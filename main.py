import itertools
import os
import os.path
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QItemSelectionModel, QStringListModel, QUrl
from PyQt5.QtGui import (
    QStandardItem,
    QStandardItemModel,
)
from PyQt5.QtWebEngineWidgets import (QWebEngineProfile, QWebEngineView)
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QMainWindow,
                             QProgressBar, QPushButton)

import wereader
from cookie import read_cookie_from_path
from ui_mainwindow import Ui_MainWindow
from frozen_dir import app_path

# root_path = os.path.abspath(os.path.dirname(__file__))
root_path = app_path()

class QmMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionShow.triggered.connect(self.toggle_mode)
        self.ui.actionSave.triggered.connect(self.save_note)
        self.ui.actionLoadShelf.triggered.connect(self.download_shelf)
        self.ui.actionLoadHot.triggered.connect(self.show_hot_note)
        self.ui.actionLoadNotes.triggered.connect(self.download_notes)
        self.ui.statusBar.hide()
        self.pbar = QProgressBar(self)
        self.pbar.setFixedWidth(500)
        self.ui.statusBar.addWidget(self.pbar)

        self.browser = QWebEngineView(self)
        self.browser.setGeometry(
            0,
            self.ui.menubar.height(),
            self.width(),
            self.height() - self.ui.menubar.height(),
        )
        self.ui.actionback.triggered.connect(self.browser.back)
        self.ui.actionforward.triggered.connect(self.browser.forward)
        self.ui.actionShelf.triggered.connect(self.view_shelf)
        self.ui.actionLibrary.triggered.connect(self.view_library)

        # 加载外部的web页面
        self.cache_path = os.path.join(root_path, "cache")
        if not os.path.exists(self.cache_path):
            os.mkdir(self.cache_path)

        # 设置缓存目录
        default_profile = QWebEngineProfile.defaultProfile()
        default_profile.setCachePath(self.cache_path)
        default_profile.setPersistentStoragePath(self.cache_path)

        # 记录上次阅读位置
        self.history_url_file = os.path.join(self.cache_path,"history.txt")
        if not os.path.exists(self.history_url_file):
            url = QUrl("https://weread.qq.com/")
        else:
            with open(self.history_url_file,'r') as f:
                url = QUrl(f.read().strip())

        self.browser.urlChanged.connect(self.update_lastpage) # 每次改变都更新还是退出的时候更新

        self.browser.load(url)
        self.model = QStringListModel(self)
        self.item_model = QStandardItemModel(self)
        self.select_model = QItemSelectionModel(self.item_model)
        self.ui.tableView.setModel(self.item_model)
        self.ui.tableView.setSelectionModel(self.select_model)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.is_reading_mode = True
        self.note_dir = os.path.join(root_path, "notes")
        if not os.path.exists(self.note_dir):
            os.mkdir(self.note_dir)

        try:
            self.update_cookies()
            self.booklist = wereader.get_bookshelf(self.cookies)
            self.books = itertools.cycle(self.booklist)
            self.curBook = self.booklist[0]
        except Exception:
            self.curBook = None
            self.booklist = None

    def update_cookies(self):
        self.cookies = read_cookie_from_path(self.cache_path + "/Cookies")

    def update_lastpage(self):
        with open(self.history_url_file,'w') as f:
            f.write(self.browser.history().currentItem().url().toString())

    def resizeEvent(self, a0):
        self.browser.resize(
            self.width(),
            self.height() - self.ui.menubar.height(),
        )
        self.ui.splitter_2.resize(
            self.width() - 10,
            self.height() - self.ui.menubar.height(),
        )

        self.ui.tableView.resize(
            self.ui.splitter.width(), self.ui.splitter.height() // 2
        )

    def on_listView_clicked(self, index):
        self.curBook = self.booklist[index.row()]
        self.on_curBook_changed()

    def on_tableView_clicked(self, index):
        self.curBook = self.booklist[index.row()]
        self.on_curBook_changed()

    def on_curBook_changed(self):
        self.ui.noteEdit.clear()
        note = self.get_note(self.curBook.bookId)
        self.ui.noteEdit.setText(note)

    def show_hot_note(self):
        self.ui.noteEdit.clear()
        note = self.get_hot_note(self.curBook.bookId)
        self.ui.noteEdit.setText(note)

    def get_note(self, id):
        note_name = os.path.join(self.note_dir, "%s.md" % id)
        if os.path.exists(note_name):
            with open(note_name, "r", encoding="utf-8") as f:
                return f.read()
        else:
            return wereader.get_bookmarklist(id, cookies=self.cookies)

    def get_hot_note(self, id):
        note_name = os.path.join(self.note_dir, "%s_hot.md" % id)
        if os.path.exists(note_name):
            with open(note_name, "r", encoding="utf-8") as f:
                return f.read()
        else:
            return wereader.get_bestbookmarks(id, cookies=self.cookies)

    def on_nextButton_clicked(self):
        self.curBook = next(self.books)
        self.on_curBook_changed()

    def save_note(self):
        text = self.ui.noteEdit.toPlainText()
        note_name = os.path.join(self.note_dir, "%s.md" % self.curBook.bookId)
        with open(note_name, "w", encoding="utf-8") as f:
            f.write(text)

    def toggle_mode(self):
        if self.is_reading_mode:
            self.browser.setVisible(False)
            self.ui.actionShow.setText("切换至阅读模式")
            self.is_reading_mode = False
        else:
            self.browser.setVisible(True)
            self.ui.actionShow.setText("切换至笔记模式")
            self.is_reading_mode = True

    def download_shelf(self):
        """加载书架时默认已经登录，重新获取cookie"""
        if not self.booklist:
            self.update_cookies()
            self.booklist = wereader.get_bookshelf(self.cookies)
            self.books = itertools.cycle(self.booklist)
        self.init_model()

    def init_model(self):
        self.model.setStringList([b.title for b in self.booklist])
        self.ui.listView.setModel(self.model)
        self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        rows = len(self.booklist)
        cols = 3
        self.item_model.setRowCount(rows)
        self.item_model.setColumnCount(cols)
        for i in range(rows):
            try:
                self.item_model.setItem(i, 0,
                                        QStandardItem(self.booklist[i].bookId))
                self.item_model.setItem(i, 1,
                                        QStandardItem(self.booklist[i].title))
                self.item_model.setItem(i, 2,
                                        QStandardItem(self.booklist[i].author))
            except Exception as e:
                print(e)
        self.ui.tableView.setModel(self.item_model)
        w = self.ui.splitter.width() // 10
        self.ui.tableView.setColumnWidth(0, 1 * w)
        self.ui.tableView.setColumnWidth(1, 6 * w)
        self.ui.tableView.setColumnWidth(2, 3 * w)
        self.ui.tableView.setSelectionModel(self.select_model)

    # def view(self):
    #     img = cv2.imread(next(self.images))  # 读取图像
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
    #     w, h = self.ui.graphicsView.width(), self.ui.graphicsView.height()
    #     img = cv2.resize(img, (w, h))
    #     frame = QImage(img, w, h, QImage.Format_RGB888)
    #     pix = QPixmap.fromImage(frame)
    #     self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
    #     # self.item.setScale(self.zoomscale)
    #     self.scene = QGraphicsScene()  # 创建场景
    #     self.scene.addItem(self.item)
    #     self.ui.graphicsView.setScene(self.scene)  # 将场景添加至视图

    def download_notes(self):
        self.ui.actionLoadNotes.setDisabled(True)
        self.ui.statusBar.show()
        self.pbar.show()
        self.pbar.setMaximum(len(self.booklist))
        for i, book in enumerate(self.booklist):
            self.pbar.setValue(i)
            try:
                note_name = os.path.join(self.note_dir, "%s.md" % book.bookId)
                if os.path.exists(note_name):
                    continue
                note = self.get_note(book.bookId)
                if note.strip():
                    with open(note_name, 'w', encoding='utf-8') as f:
                        f.write(note)
            except Exception as e:
                print(e)

        self.pbar.hide()
        self.ui.statusBar.hide()

    def view_library(self):
        self.browser.load(QUrl("https://weread.qq.com/web/category"))

    def view_shelf(self):
        self.browser.load(QUrl("https://weread.qq.com/web/shelf"))



app = QApplication(sys.argv)
mMainWindow = QmMainWindow()
mMainWindow.show()
sys.exit(app.exec_())
