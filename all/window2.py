# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.subject_search = QtWidgets.QComboBox(self.centralwidget)
        self.subject_search.setGeometry(QtCore.QRect(70, 150, 150, 25))
        self.subject_search.setObjectName("subject_search")
        self.class_search = QtWidgets.QComboBox(self.centralwidget)
        self.class_search.setGeometry(QtCore.QRect(360, 150, 100, 26))
        self.class_search.setObjectName("class_search")
        self.type_search = QtWidgets.QComboBox(self.centralwidget)
        self.type_search.setGeometry(QtCore.QRect(240, 150, 100, 25))
        self.type_search.setObjectName("type_search")
        self.pushButton_search1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search1.setGeometry(QtCore.QRect(480, 150, 100, 26))
        self.pushButton_search1.setObjectName("pushButton_search1")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 210, 851, 411))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_search1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search1.setGeometry(QtCore.QRect(70, 40, 510, 25))
        self.lineEdit_search1.setObjectName("lineEdit_search1")
        self.pushButton_search2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search2.setGeometry(QtCore.QRect(600, 39, 100, 25))
        self.pushButton_search2.setObjectName("pushButton_search2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 380, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 105, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 80, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_search3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search3.setGeometry(QtCore.QRect(704, 110, 101, 25))
        self.pushButton_search3.setObjectName("pushButton_search3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 140, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_search4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search4.setGeometry(QtCore.QRect(704, 165, 100, 25))
        self.pushButton_search4.setObjectName("pushButton_search4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Olimp_search"))
        self.pushButton_search1.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_search2.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Сохранить конкретную олимпиаду по её названию"))
        self.label_2.setText(_translate("MainWindow", "Поиск всех олимпиад по данным критериям"))
        self.label_3.setText(_translate("MainWindow", "Просмотр всех сохранённых олимпиад"))
        self.pushButton_search3.setText(_translate("MainWindow", "Нажми"))
        self.label_4.setText(_translate("MainWindow", "Удаление конкретной олимпиады"))
        self.pushButton_search4.setText(_translate("MainWindow", "Нажми"))
