from PyQt5 import QtCore, QtGui, QtWidgets
from Registration import Ui_Registration
from Authentication import Ui_testAuthentication
from result import Ui_Result
from adminAuthentication import Ui_testAuthentication2
# import pandas
# from openpyxl import Workbook,load_workbook
# from openpyxl.utils.dataframe import dataframe_to_rows

class Ui_Menu(object):

    def btn(self,fun):
        self.window=QtWidgets.QMainWindow()
        self.ui=fun()
        self.ui.setupUi(self.window)
        #Menu.hide()
        self.window.show()          
    
    
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.B_reg = QtWidgets.QPushButton(self.centralwidget)
        self.B_reg.setGeometry(QtCore.QRect(20, 170, 171, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_reg.sizePolicy().hasHeightForWidth())
        self.B_reg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.B_reg.setFont(font)
        self.B_reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_reg.setMouseTracking(False)
        self.B_reg.setObjectName("B_reg")
        self.B_result = QtWidgets.QPushButton(self.centralwidget)
        self.B_result.setGeometry(QtCore.QRect(20, 440, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.B_reg.clicked.connect(lambda:self.btn(Ui_Registration))
        
        self.B_result.setFont(font)
        self.B_result.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_result.setObjectName("B_result")
        self.B_summary = QtWidgets.QPushButton(self.centralwidget)
        self.B_summary.setGeometry(QtCore.QRect(20, 350, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
      
        self.B_result.clicked.connect(lambda:self.btn(Ui_Result))
        
        self.B_summary.setFont(font)
        self.B_summary.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_summary.setObjectName("B_summary")
        self.B_test = QtWidgets.QPushButton(self.centralwidget)
        self.B_test.setGeometry(QtCore.QRect(20, 260, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.B_summary.clicked.connect(lambda:self.btn(Ui_testAuthentication2))
        
        self.B_test.setFont(font)
        self.B_test.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_test.setObjectName("B_test")
        self.B_exit = QtWidgets.QPushButton(self.centralwidget)
        self.B_exit.setGeometry(QtCore.QRect(630, 460, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        
        self.B_test.clicked.connect(lambda:self.btn(Ui_testAuthentication))
        
        self.B_exit.setFont(font)
        self.B_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_exit.setObjectName("B_exit")
        self.L_quiz = QtWidgets.QLabel(self.centralwidget)
        self.L_quiz.setGeometry(QtCore.QRect(200, 0, 401, 191))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        self.B_exit.clicked.connect(Menu.close)
        
        self.L_quiz.setFont(font)
        self.L_quiz.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.L_quiz.setScaledContents(True)
        self.L_quiz.setAlignment(QtCore.Qt.AlignCenter)
        self.L_quiz.setObjectName("L_quiz")
        self.bg_image = QtWidgets.QLabel(self.centralwidget)
        self.bg_image.setGeometry(QtCore.QRect(10, 0, 781, 571))
        self.bg_image.setText("")
        self.bg_image.setPixmap(QtGui.QPixmap("Assets\\mainFrontEnd\\background.jpg"))
        self.bg_image.setScaledContents(True)
        self.bg_image.setObjectName("bg_image")
        self.bg_image.raise_()
        self.B_reg.raise_()
        self.B_result.raise_()
        self.B_summary.raise_()
        self.B_test.raise_()
        self.B_exit.raise_()
        self.L_quiz.raise_()
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)
        

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.B_reg.setToolTip(_translate("Menu", "A new user? register here"))
        self.B_reg.setText(_translate("Menu", "Register"))
        self.B_result.setToolTip(_translate("Menu", "View your results"))
        self.B_result.setText(_translate("Menu", "Result"))
        self.B_summary.setToolTip(_translate("Menu", "Only for admins!"))
        self.B_summary.setText(_translate("Menu", "Summary"))
        self.B_test.setToolTip(_translate("Menu", "Wanna try?"))
        self.B_test.setText(_translate("Menu", "Take test"))
        self.B_exit.setText(_translate("Menu", "exit"))
        self.L_quiz.setText(_translate("Menu", "Quiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

