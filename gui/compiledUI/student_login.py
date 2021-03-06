from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sqlite3
import assest.resource_rc
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Ui_studentLoginWindow(object):
    def setupUi(self, studentLoginWindow):
        studentLoginWindow.setObjectName("studentLoginWindow")
        studentLoginWindow.resize(300, 175)
        self.centralwidget = QtWidgets.QWidget(studentLoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 241, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 2, 1, 1, 1)
        self.username_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 1, 0, 1, 1)
        self.password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 2, 0, 1, 1)
        self.username_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username_input.setObjectName("username_input")
        self.gridLayout.addWidget(self.username_input, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(8)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 3, 1, 1, 1)
        self.student_label = QtWidgets.QLabel(self.centralwidget)
        self.student_label.setGeometry(QtCore.QRect(10, 10, 211, 31))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.student_label.setFont(font)
        self.student_label.setObjectName("student_label")
        studentLoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(studentLoginWindow)
        self.statusbar.setObjectName("statusbar")
        studentLoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(studentLoginWindow)
        QtCore.QMetaObject.connectSlotsByName(studentLoginWindow)
        self.login_button.clicked.connect(self.Handlelogin)
     
    def retranslateUi(self, studentLoginWindow):
        _translate = QtCore.QCoreApplication.translate
        studentLoginWindow.setWindowTitle(_translate("studentLoginWindow", "Student Login"))
        self.username_label.setText(_translate("studentLoginWindow", "Username:"))
        self.password_label.setText(_translate("studentLoginWindow", "Password:"))
        self.login_button.setText(_translate("studentLoginWindow", "LOGIN"))
        self.student_label.setText(_translate("studentLoginWindow", "Student LOGIN"))
    
       
    def Handlelogin(self):
        self.username = ""
        self.password = ""

        self.username = self.username_input.text()  
        self.password = self.password_input.text()
       
        try:
            self.conn = sqlite3.connect("data/database.db")
            self.c = self.conn.cursor()
            self.c.execute('SELECT * from "students" WHERE "name" = ? AND "password" = ?',  (self.username,self.password))
            if self.c.fetchone() is not None:
                print("login success!")
            else:
                print("Login Failed!")
            
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find student from the database.')
            
