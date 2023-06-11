# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QListView,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QSplitter,
    QStatusBar,
    QTableView,
    QTextEdit,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 704)
        MainWindow.setBaseSize(QSize(1080, 720))
        icon = QIcon()
        icon.addFile(":/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.actionLoadNotes = QAction(MainWindow)
        self.actionLoadNotes.setObjectName("actionLoadNotes")
        self.actionShow = QAction(MainWindow)
        self.actionShow.setObjectName("actionShow")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAuthor = QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionLoadShelf = QAction(MainWindow)
        self.actionLoadShelf.setObjectName("actionLoadShelf")
        self.actionLoadHot = QAction(MainWindow)
        self.actionLoadHot.setObjectName("actionLoadHot")
        self.actionLoadCover = QAction(MainWindow)
        self.actionLoadCover.setObjectName("actionLoadCover")
        self.actionback = QAction(MainWindow)
        self.actionback.setObjectName("actionback")
        self.actionforward = QAction(MainWindow)
        self.actionforward.setObjectName("actionforward")
        self.actionShelf = QAction(MainWindow)
        self.actionShelf.setObjectName("actionShelf")
        self.actionLibrary = QAction(MainWindow)
        self.actionLibrary.setObjectName("actionLibrary")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.browser = QWidget(MainWindow)
        self.browser.setObjectName("browser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browser.sizePolicy().hasHeightForWidth())
        self.browser.setSizePolicy(sizePolicy)
        self.browser.setBaseSize(QSize(1080, 700))
        self.browser.setAutoFillBackground(True)
        self.splitter_2 = QSplitter(self.browser)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_2.setGeometry(QRect(5, 0, 1070, 700))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.listView = QListView(self.splitter)
        self.listView.setObjectName("listView")
        self.splitter.addWidget(self.listView)
        self.tableView = QTableView(self.splitter)
        self.tableView.setObjectName("tableView")
        self.splitter.addWidget(self.tableView)
        self.splitter_2.addWidget(self.splitter)
        self.noteEdit = QTextEdit(self.splitter_2)
        self.noteEdit.setObjectName("noteEdit")
        self.splitter_2.addWidget(self.noteEdit)
        MainWindow.setCentralWidget(self.browser)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1072, 23))
        self.menuTool = QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuNote = QMenu(self.menubar)
        self.menuNote.setObjectName("menuNote")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuNote.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuTool.addAction(self.actionLoadShelf)
        self.menuTool.addSeparator()
        self.menuTool.addAction(self.actionLoadNotes)
        self.menuTool.addAction(self.actionLoadCover)
        self.menuNote.addSeparator()
        self.menuNote.addAction(self.actionShow)
        self.menuNote.addAction(self.actionSave)
        self.menuNote.addSeparator()
        self.menuNote.addAction(self.actionLoadHot)
        self.menuNote.addAction(self.actionOpen)
        self.menuAbout.addAction(self.actionAuthor)
        self.menuAbout.addAction(self.actionLicense)
        self.menuView.addAction(self.actionback)
        self.menuView.addAction(self.actionforward)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShelf)
        self.menuView.addAction(self.actionLibrary)
        self.menuView.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", "\u5fae\u4fe1\u8bfb\u4e66\u52a9\u624b-wereader", None
            )
        )
        self.actionLoadNotes.setText(
            QCoreApplication.translate(
                "MainWindow", "\u4e0b\u8f7d\u5168\u90e8\u7b14\u8bb0", None
            )
        )
        self.actionShow.setText(
            QCoreApplication.translate(
                "MainWindow", "\u5207\u6362\u7b14\u8bb0\u6a21\u5f0f", None
            )
        )
        # if QT_CONFIG(shortcut)
        self.actionShow.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Tab", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSave.setText(
            QCoreApplication.translate("MainWindow", "\u4fdd\u5b58\u7b14\u8bb0", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionAuthor.setText(
            QCoreApplication.translate("MainWindow", "Author <arry_lee@qq.com>", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionAuthor.setToolTip(
            QCoreApplication.translate("MainWindow", "Author", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.actionLicense.setText(
            QCoreApplication.translate("MainWindow", "License", None)
        )
        self.actionLoadShelf.setText(
            QCoreApplication.translate("MainWindow", "\u52a0\u8f7d\u4e66\u67b6", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionLoadShelf.setToolTip(
            QCoreApplication.translate("MainWindow", "Download shelf", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.actionLoadHot.setText(
            QCoreApplication.translate("MainWindow", "\u70ed\u95e8\u7b14\u8bb0", None)
        )
        self.actionLoadCover.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u8f7d\u5c01\u9762", None)
        )
        self.actionback.setText(
            QCoreApplication.translate("MainWindow", "\u540e\u9000", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionback.setToolTip(
            QCoreApplication.translate("MainWindow", "\u540e\u9000", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionback.setShortcut(QCoreApplication.translate("MainWindow", "B", None))
        # endif // QT_CONFIG(shortcut)
        self.actionforward.setText(
            QCoreApplication.translate("MainWindow", "\u524d\u8fdb", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionforward.setToolTip(
            QCoreApplication.translate("MainWindow", "\u524d\u8fdb", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionforward.setShortcut(
            QCoreApplication.translate("MainWindow", "F", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShelf.setText(
            QCoreApplication.translate("MainWindow", "\u4e66\u67b6", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionShelf.setShortcut(
            QCoreApplication.translate("MainWindow", "S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionLibrary.setText(
            QCoreApplication.translate("MainWindow", "\u4e66\u57ce", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionLibrary.setShortcut(
            QCoreApplication.translate("MainWindow", "L", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u5f00\u7b14\u8bb0", None)
        )
        self.menuTool.setTitle(
            QCoreApplication.translate("MainWindow", "\u5de5\u5177", None)
        )
        self.menuNote.setTitle(
            QCoreApplication.translate("MainWindow", "\u7b14\u8bb0", None)
        )
        self.menuAbout.setTitle(
            QCoreApplication.translate("MainWindow", "\u5173\u4e8e", None)
        )
        self.menuView.setTitle(
            QCoreApplication.translate("MainWindow", "\u89c6\u56fe", None)
        )

    # retranslateUi
