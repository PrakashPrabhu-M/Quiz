# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Authentication.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Summary import Ui_Result

class Ui_testAuthentication2(object):
    def nxt(self):
        try:
            if self.LE_password.text()=='toor' and self.LE_id.text()=='root':
                self.window=QtWidgets.QMainWindow()
                self.ui=Ui_Result()
                self.ui.setupUi(self.window)
                #testAuthentication.hide()
                self.window.show()
            else:
                msg=QMessageBox()
                msg.setWindowTitle('Info')
                msg.setText('Invalid credentials')
                msg.setIcon(QMessageBox.Information)
                x=msg.exec_()
        except:
            msg=QMessageBox()
            msg.setWindowTitle('Info')
            msg.setText('Invalid credentials')
            msg.setIcon(QMessageBox.Critical)
            x=msg.exec_()
    
    def setupUi(self, testAuthentication):
        testAuthentication.setObjectName("testAuthentication")
        testAuthentication.resize(664, 214)
        self.centralwidget = QtWidgets.QWidget(testAuthentication)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_image = QtWidgets.QLabel(self.centralwidget)
        self.bg_image.setGeometry(QtCore.QRect(0, 5, 661, 161))
        self.bg_image.setText("")
        self.bg_image.setPixmap(QtGui.QPixmap(r"Assets/Take test/background.png"))
        self.bg_image.setScaledContents(False)
        self.bg_image.setObjectName("bg_image")
        self.L_adminId = QtWidgets.QLabel(self.centralwidget)
        self.L_adminId.setGeometry(QtCore.QRect(150, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.L_adminId.setFont(font)
        self.L_adminId.setObjectName("L_adminId")
        self.LE_id = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_id.setGeometry(QtCore.QRect(310, 21, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.LE_id.setFont(font)
        self.LE_id.setObjectName("LE_id")
        self.B_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.B_cancel.setGeometry(QtCore.QRect(320, 120, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.B_cancel.setFont(font)
        self.B_cancel.setObjectName("B_cancel")
        
        self.B_cancel.clicked.connect(testAuthentication.close)
        
        self.B_next = QtWidgets.QPushButton(self.centralwidget)
        self.B_next.setGeometry(QtCore.QRect(430, 120, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.B_next.setFont(font)
        self.B_next.setObjectName("B_next")
        
        self.B_next.clicked.connect(self.nxt)
        
        self.L_password = QtWidgets.QLabel(self.centralwidget)
        self.L_password.setGeometry(QtCore.QRect(150, 50, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.L_password.setFont(font)
        self.L_password.setObjectName("L_password")
        self.LE_password = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_password.setGeometry(QtCore.QRect(310, 70, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.LE_password.setFont(font)
        self.LE_password.setObjectName("LE_password")
        testAuthentication.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(testAuthentication)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 26))
        self.menubar.setObjectName("menubar")
        testAuthentication.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(testAuthentication)
        self.statusbar.setObjectName("statusbar")
        testAuthentication.setStatusBar(self.statusbar)

        self.retranslateUi(testAuthentication)
        QtCore.QMetaObject.connectSlotsByName(testAuthentication)

    def retranslateUi(self, testAuthentication):
        _translate = QtCore.QCoreApplication.translate
        testAuthentication.setWindowTitle(_translate("testAuthentication", "Authentication"))
        self.L_adminId.setText(_translate("testAuthentication", "Admin id:"))
        self.LE_id.setToolTip(_translate("testAuthentication", "Your id number"))
        self.B_cancel.setText(_translate("testAuthentication", "Cancel"))
        self.B_next.setText(_translate("testAuthentication", "Next >>"))
        self.L_password.setText(_translate("testAuthentication", "Password:"))
        self.LE_password.setToolTip(_translate("testAuthentication", "Your id number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testAuthentication = QtWidgets.QMainWindow()
    ui = Ui_testAuthentication2()
    ui.setupUi(testAuthentication)
    testAuthentication.show()
    sys.exit(app.exec_())

