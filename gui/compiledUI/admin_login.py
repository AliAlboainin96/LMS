from PyQt5 import QtCore, QtGui, QtWidgets
import json
import assest.resource_rc
import sqlite3

class Ui_adminLoginWindow(object):
    def setupUi(self, adminLoginWindow):
        adminLoginWindow.setObjectName("adminLoginWindow")
        adminLoginWindow.resize(300, 175)
        self.centralwidget = QtWidgets.QWidget(adminLoginWindow)
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
        self.admin_label = QtWidgets.QLabel(self.centralwidget)
        self.admin_label.setGeometry(QtCore.QRect(10, 10, 211, 31))
       
        font = QtGui.QFont()
        font.setPointSize(16)
        self.admin_label.setFont(font)
        self.admin_label.setObjectName("admin_label")
        adminLoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminLoginWindow)
        self.statusbar.setObjectName("statusbar")
        adminLoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(adminLoginWindow)
        QtCore.QMetaObject.connectSlotsByName(adminLoginWindow)

        self.login_button.clicked.connect(self.Handlelogin)
    def retranslateUi(self, adminLoginWindow):
        _translate = QtCore.QCoreApplication.translate
        adminLoginWindow.setWindowTitle(_translate("adminLoginWindow", "Admin Login"))
        self.username_label.setText(_translate("adminLoginWindow", "Username:"))
        self.password_label.setText(_translate("adminLoginWindow", "Password:"))
        self.login_button.setText(_translate("adminLoginWindow", "LOGIN"))
        self.admin_label.setText(_translate("adminLoginWindow", "Admin LOGIN"))
        
    def Handlelogin(self):
        with open("data/admin_account.json") as file:
            data = json.load(file)
            
            if self.username_input.text() == data['username'] and self.password_input.text() == data['password']:
                self.accept = True    
                print("Welcome Back!")
            
            else:
                print('Username or Password are wrong')
    
        