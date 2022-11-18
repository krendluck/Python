# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
import sys
import os
import mysql.connector
from dotenv import load_dotenv
from search import search

class CustWidget(QtWidgets.QWidget):
    def __init__(self,parent=None) -> None:
        super(CustWidget,self).__init__(parent)
        self.resize(500,400)
        self.setMinimumSize(500,400)
        self.setMaximumSize(500,400)
        
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 250,200))

        #屏幕居中显示
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),int((screen.height() - size.height()) / 2))
        self.widget.setObjectName("widget")

        #窗口内部居中显示
        translateSize = self.widget.geometry()
        self.widget.move(int((size.width() - translateSize.width()) / 2),int((size.height() - translateSize.height()) / 2))

        self.vlayout = QtWidgets.QVBoxLayout(self.widget)
        self.vlayout.setContentsMargins(0, 0, 0, 0)

        self.character = QtWidgets.QLineEdit(self.widget)
        self.character.setObjectName('charater')
        self.character.setMinimumSize(150,30)
        self.character.setMaximumSize(150,30)

        self.searchButton = QtWidgets.QPushButton("search",self.widget)
        self.searchButton.setObjectName('searchButton')
        self.searchButton.setMinimumSize(100,30)
        self.searchButton.setMaximumSize(100,30)

        self.hlayout = QtWidgets.QHBoxLayout() 
        self.hlayout.addWidget(self.character)
        self.hlayout.addWidget(self.searchButton)

        self.translate = QtWidgets.QLabel("translate",self)
        self.translate.setObjectName("translate")
        self.translate.setWordWrap(True)
        
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addWidget(self.translate)

        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_searchButton_clicked(self):
        character = self.character.text()
        search(self,character,cursor)
       
if __name__ == '__main__':
    load_dotenv()
    connection = mysql.connector.connect(
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
        user=os.getenv("NAME"),
        password=os.getenv("PASSWORD"),
        ssl_ca=os.getenv("SSL_CERT")
    )
    cursor = connection.cursor()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CustWidget()
    MainWindow.show()
    sys.exit(app.exec())
