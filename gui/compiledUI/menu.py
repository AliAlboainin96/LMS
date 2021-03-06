from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from compiledUI.admin_login import *
from compiledUI.student_login import *
from compiledUI.student_signIn import *
import assest.resource_rc
import sys 
import os

class Ui_MenuWindow(object):
   
    def openAdminLoginWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_adminLoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openStudentLoginWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_studentLoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openStudentSignInWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_SignInWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openGuestViewWindow():
        self.window = QMainWindow()
        self.ui = Ui_adminLoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(375, 300)
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.admin_login = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.admin_login.setFont(font)
        self.admin_login.setObjectName("admin_login")
        self.gridLayout.addWidget(self.admin_login, 0, 1, 1, 1)
        self.admin_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.admin_label.setFont(font)
        self.admin_label.setObjectName("admin_label")
        self.gridLayout.addWidget(self.admin_label, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 221, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.student_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.student_label.setFont(font)
        self.student_label.setObjectName("student_label")
        self.gridLayout_2.addWidget(self.student_label, 0, 0, 1, 1)
        self.student_login = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.student_login.setFont(font)
        self.student_login.setObjectName("student_login")
        self.gridLayout_2.addWidget(self.student_login, 0, 1, 1, 1)
        self.student_signin = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.student_signin.setFont(font)
        self.student_signin.setObjectName("student_signin")
        self.gridLayout_2.addWidget(self.student_signin, 1, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 200, 221, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.guest_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guest_label.setFont(font)
        self.guest_label.setObjectName("guest_label")
        self.gridLayout_3.addWidget(self.guest_label, 0, 0, 1, 1)
        self.guest_view = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.guest_view.setFont(font)
        self.guest_view.setObjectName("guest_view")
        self.gridLayout_3.addWidget(self.guest_view, 0, 1, 1, 1)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(250, -10, 111, 151))
        self.logo.setObjectName("logo")
        MenuWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

        

        self.admin_login.clicked.connect(self.openAdminLoginWindow)
        self.student_login.clicked.connect(self.openStudentLoginWindow)
        self.student_signin.clicked.connect(self.openStudentSignInWindow)
        self.guest_view.clicked.connect(self.openGuestViewWindow)

        

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "LMS"))
        self.admin_login.setText(_translate("MenuWindow", "Login"))
        self.admin_label.setText(_translate("MenuWindow", "Admin:"))
        self.student_label.setText(_translate("MenuWindow", "Student:"))
        self.student_login.setText(_translate("MenuWindow", "Login"))
        self.student_signin.setText(_translate("MenuWindow", "Sign In"))
        self.guest_label.setText(_translate("MenuWindow", "Guest:"))
        self.guest_view.setText(_translate("MenuWindow", "View"))
        self.logo.setText(_translate("MenuWindow", "<html><head/><body><p><img src=\":/image/logo.png\"/></p></body></html>"))