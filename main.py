import glob
import itertools
import os.path
import sys
import cv2
import os

from PyQt5.QtCore import (QDir, QItemSelectionModel, QStringListModel, QUrl, Qt,
                          pyqtSlot)
from PyQt5.QtWebEngineWidgets import (QWebEngineSettings, QWebEngineView,
                                      QWebEngineProfile)
from PyQt5.QtWidgets import (QAbstractItemView, QFileSystemModel,
                             QGraphicsPixmapItem,
                             QGraphicsScene, QWidget,
                             QApplication)
from PyQt5.QtGui import (QImage, QPalette, QIcon, QPixmap, QStandardItem,
                         QStandardItemModel)


from ui_weareder import Ui_Form

from cookie import read_cookie_from_path
import wereader


class QmWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.label = "wereader"
        self.ui.lineEdit.setStyleSheet('border-radius: 6px; border: 2px groove gray;')
        self.ui.label.setText(self.label)
        # self.ui.pushButton_2.clicked.connect(self.init_model_from_book_shelf)
        self.images = itertools.cycle(glob.iglob('static/*png'))
        self.browser = QWebEngineView(self)
        self.browser.setGeometry(0,0,800,720)

        # 加载外部的web页面
        self.cache_path = "cache"
        if not os.path.exists(self.cache_path):
            os.mkdir(self.cache_path)
        self.note_dir = "notes"
        if not os.path.exists(self.note_dir):
            os.mkdir(self.note_dir)
        # 设置缓存目录
        default_profile = QWebEngineProfile.defaultProfile()
        default_profile.setCachePath(self.cache_path)
        default_profile.setPersistentStoragePath(self.cache_path)
        default_cookie = default_profile.cookieStore()

        self.cookies = read_cookie_from_path(self.cache_path + "/Cookies")

        self.browser.load(QUrl('https://weread.qq.com/'))
        self.isBrowserVisible = True
        self.model = QStringListModel(self)
        self.item_model = QStandardItemModel(self)
        self.select_model = QItemSelectionModel(self.item_model)
        self.ui.tableView.setModel(self.item_model)
        self.ui.tableView.setSelectionModel(self.select_model)
        self.ui.tableView.setAlternatingRowColors(True)


        self.curBook = None
        self.booklist = None
        try:
            self.booklist = wereader.get_bookshelf(self.cookies)
            self.books = itertools.cycle(self.booklist)
        except Exception as e:
            default_cookie.deleteAllCookies()
            self.browser.reload()

        self.is_reading_mode = True

    def update_cookies(self):
        self.cookies = read_cookie_from_path(self.cache_path + "/Cookies")

    def on_listView_clicked(self,index):
        self.curBook = self.booklist[index.row()]
        self.on_curBook_changed()

    def on_tableView_clicked(self,index):
        self.curBook = self.booklist[index.row()]
        self.on_curBook_changed()

    def on_curBook_changed(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setPlainText(self.get_note(self.curBook.bookId))


    def get_note(self,id):
        note_name = os.path.join(self.note_dir,"%s.md"%id)
        if os.path.exists(note_name):
            with open(note_name,'r',encoding='utf-8') as f:
                return f.read()
        else:
            return wereader.get_bookmarklist(id,cookies=self.cookies)

    def on_nextButton_clicked(self):
        self.curBook = next(self.books)
        self.on_curBook_changed()

    def on_saveButton_clicked(self):
        text = self.ui.plainTextEdit.toPlainText()
        note_name = os.path.join(self.note_dir, "%s.md" % self.curBook.bookId)
        with open(note_name,'w',encoding='utf-8') as f:
            f.write(text)

    def on_radioButton_toggled(self):
        if self.is_reading_mode:
            self.browser.setVisible(False)
            self.ui.radioButton.setText("笔记模式")
            self.is_reading_mode = False
        else:
            self.browser.setVisible(True)
            self.ui.radioButton.setText("阅读模式")
            self.is_reading_mode = True

    def on_searchButton_clicked(self):
        self.browser.setVisible(True)

    def on_loadButton_clicked(self):
        """加载书架时默认已经登录，重新获取cookie"""
        if not self.booklist:
            self.update_cookies()
            self.booklist = wereader.get_bookshelf(self.cookies)
            self.books = itertools.cycle(self.booklist)

        self.model.setStringList([b.title for b in self.booklist])
        self.ui.listView.setModel(self.model)
        self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.init_model()

    def init_model(self):
        rows = len(self.booklist)
        cols = 3
        self.item_model.setRowCount(rows)
        self.item_model.setColumnCount(cols)
        for i in range(rows):
            try:
                self.item_model.setItem(i,0,QStandardItem(self.booklist[i].bookId))
                self.item_model.setItem(i,1, QStandardItem(self.booklist[i].title))
                self.item_model.setItem(i,2, QStandardItem(self.booklist[i].author))
            except Exception as e:
                print(e)
        self.ui.tableView.setModel(self.item_model)
        self.ui.tableView.setSelectionModel(self.select_model)


    def view(self):
        img = cv2.imread(next(self.images))  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        w,h = self.ui.graphicsView.width(),self.ui.graphicsView.height()
        img = cv2.resize(img,(w,h))
        frame = QImage(img, w, h, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)  # 将场景添加至视图


    def do_change_background(self):
        pal = self.ui.lineEdit.palette()
        pal.setColor(QPalette.Text,Qt.black)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mWidget = QmWidget()
    mWidget.show()
    # mWidget.setBtnText("example")
    sys.exit(app.exec_())