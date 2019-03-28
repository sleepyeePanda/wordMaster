# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 339)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-image:url(:/img/bg.png)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 301, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("background:transparent")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.enrollButton = QtWidgets.QPushButton(self.page_main)
        self.enrollButton.setGeometry(QtCore.QRect(50, 60, 201, 41))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enrollButton.setFont(font)
        self.enrollButton.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:3px solid white;\n"
"border-radius :20px;\n"
"background-color:white}\n"
"QPushButton{color:white;\n"
"border:3px solid white;\n"
"border-radius :20px;\n"
"background:transparent}\n"
"")
        self.enrollButton.setObjectName("enrollButton")
        self.memorizeButton = QtWidgets.QPushButton(self.page_main)
        self.memorizeButton.setGeometry(QtCore.QRect(50, 110, 201, 41))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.memorizeButton.setFont(font)
        self.memorizeButton.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:3px solid white;\n"
"border-radius :20px;\n"
"background-color:white}\n"
"QPushButton{color:white;\n"
"border:3px solid white;\n"
"border-radius :20px;\n"
"background:transparent}\n"
"")
        self.memorizeButton.setObjectName("memorizeButton")
        self.gameButton = QtWidgets.QPushButton(self.page_main)
        self.gameButton.setGeometry(QtCore.QRect(50, 160, 201, 41))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gameButton.setFont(font)
        self.gameButton.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:3px solid white;\n"
"border-radius :20px;\n"
"background-color:white}\n"
"QPushButton{color:white;\n"
"border:3px solid white;\n"
"border-radius :20px;\n"
"background:transparent}\n"
"")
        self.gameButton.setObjectName("gameButton")
        self.recordButton = QtWidgets.QPushButton(self.page_main)
        self.recordButton.setGeometry(QtCore.QRect(50, 210, 201, 41))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.recordButton.setFont(font)
        self.recordButton.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:3px solid white;\n"
"border-radius :20px;\n"
"background-color:white}\n"
"QPushButton{color:white;\n"
"border:3px solid white;\n"
"border-radius :20px;\n"
"background:transparent}\n"
"")
        self.recordButton.setObjectName("recordButton")
        self.stackedWidget.addWidget(self.page_main)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 261, 161))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{background:transparent;\n"
"color:white;\n"
"border:1px solid rgb(70,70,70);\n"
"border-radius:7px}\n"
"QTableWidget:section{\n"
"border:1px solid black;\n"
"border-radius:7px;\n"
"background:white;\n"
"color:rgb(70,70,70)}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.enterButton_1 = QtWidgets.QPushButton(self.page_2)
        self.enterButton_1.setGeometry(QtCore.QRect(228, 270, 51, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enterButton_1.setFont(font)
        self.enterButton_1.setStyleSheet("color:rgb(70,70,70);\n"
"border:2px solid rgb(70,70,70);\n"
"border-radius:12px")
        self.enterButton_1.setObjectName("enterButton_1")
        self.KorEdit = QtWidgets.QLineEdit(self.page_2)
        self.KorEdit.setGeometry(QtCore.QRect(20, 270, 201, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Light")
        font.setPointSize(12)
        self.KorEdit.setFont(font)
        self.KorEdit.setStyleSheet("color:rgb(70,70,70);\n"
"border:1px solid rgb(70,70,70);\n"
"border-radius:7px")
        self.KorEdit.setMaxLength(20)
        self.KorEdit.setObjectName("KorEdit")
        self.EngEdit = QtWidgets.QLineEdit(self.page_2)
        self.EngEdit.setGeometry(QtCore.QRect(20, 230, 261, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.EngEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Light")
        font.setPointSize(12)
        self.EngEdit.setFont(font)
        self.EngEdit.setAutoFillBackground(False)
        self.EngEdit.setStyleSheet("color:rgb(70,70,70);\n"
"border:1px solid rgb(70,70,70);\n"
"border-radius:7px")
        self.EngEdit.setMaxLength(20)
        self.EngEdit.setObjectName("EngEdit")
        self.backButton_1 = QtWidgets.QPushButton(self.page_2)
        self.backButton_1.setGeometry(QtCore.QRect(10, 5, 25, 25))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backButton_1.setFont(font)
        self.backButton_1.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background-color:white}\n"
"QPushButton{color:white;\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background:transparent}")
        self.backButton_1.setObjectName("backButton_1")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.status_2 = QtWidgets.QLabel(self.page_3)
        self.status_2.setGeometry(QtCore.QRect(110, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.status_2.setFont(font)
        self.status_2.setStyleSheet("color:rgb(70, 70, 70)")
        self.status_2.setAlignment(QtCore.Qt.AlignCenter)
        self.status_2.setObjectName("status_2")
        self.wordScreen_2 = QtWidgets.QPushButton(self.page_3)
        self.wordScreen_2.setGeometry(QtCore.QRect(0, 70, 301, 141))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.wordScreen_2.setFont(font)
        self.wordScreen_2.setStyleSheet("color:white")
        self.wordScreen_2.setObjectName("wordScreen_2")
        self.backButton_2 = QtWidgets.QPushButton(self.page_3)
        self.backButton_2.setGeometry(QtCore.QRect(10, 5, 25, 25))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backButton_2.setFont(font)
        self.backButton_2.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background-color:white}\n"
"QPushButton{color:white;\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background:transparent}")
        self.backButton_2.setObjectName("backButton_2")
        self.prev_2 = QtWidgets.QPushButton(self.page_3)
        self.prev_2.setGeometry(QtCore.QRect(10, 270, 25, 25))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.prev_2.setFont(font)
        self.prev_2.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background-color:white}\n"
"QPushButton{color:rgb(70,70,70);\n"
"border:2px solid rgb(70,70,70);\n"
"border-radius :12px;\n"
"background:transparent}")
        self.prev_2.setObjectName("prev_2")
        self.next_2 = QtWidgets.QPushButton(self.page_3)
        self.next_2.setGeometry(QtCore.QRect(260, 270, 25, 25))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.next_2.setFont(font)
        self.next_2.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background-color:white}\n"
"QPushButton{color:rgb(70,70,70);\n"
"border:2px solid rgb(70,70,70);\n"
"border-radius :12px;\n"
"background:transparent}")
        self.next_2.setObjectName("next_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.score = QtWidgets.QLabel(self.page)
        self.score.setGeometry(QtCore.QRect(80, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setStyleSheet("color:white")
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setObjectName("score")
        self.answerEdit = QtWidgets.QLineEdit(self.page)
        self.answerEdit.setGeometry(QtCore.QRect(20, 270, 201, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Light")
        font.setPointSize(12)
        self.answerEdit.setFont(font)
        self.answerEdit.setStyleSheet("color:rgb(70,70,70);\n"
"border:1px solid rgb(70,70,70);\n"
"border-radius:7px")
        self.answerEdit.setObjectName("answerEdit")
        self.wordScreen_3 = QtWidgets.QPushButton(self.page)
        self.wordScreen_3.setGeometry(QtCore.QRect(0, 90, 301, 121))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.wordScreen_3.setFont(font)
        self.wordScreen_3.setStyleSheet("color:white")
        self.wordScreen_3.setObjectName("wordScreen_3")
        self.status_3 = QtWidgets.QLabel(self.page)
        self.status_3.setGeometry(QtCore.QRect(170, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.status_3.setFont(font)
        self.status_3.setStyleSheet("color:white")
        self.status_3.setAlignment(QtCore.Qt.AlignCenter)
        self.status_3.setObjectName("status_3")
        self.backButton_3 = QtWidgets.QPushButton(self.page)
        self.backButton_3.setGeometry(QtCore.QRect(10, 5, 25, 25))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backButton_3.setFont(font)
        self.backButton_3.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background-color:white}\n"
"QPushButton{color:white;\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background:transparent}")
        self.backButton_3.setObjectName("backButton_3")
        self.enterButton_3 = QtWidgets.QPushButton(self.page)
        self.enterButton_3.setGeometry(QtCore.QRect(230, 270, 51, 31))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enterButton_3.setFont(font)
        self.enterButton_3.setStyleSheet("color:rgb(70,70,70);\n"
"border:2px solid rgb(70,70,70);\n"
"border-radius:12px")
        self.enterButton_3.setObjectName("enterButton_3")
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.recordTable = QtWidgets.QTableWidget(self.page_4)
        self.recordTable.setGeometry(QtCore.QRect(20, 60, 261, 241))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recordTable.setFont(font)
        self.recordTable.setStyleSheet("QTableWidget{background:transparent;\n"
"color:white;\n"
"border:1px solid rgb(70,70,70);\n"
"border-radius:7px}\n"
"QTableWidget:section{\n"
"border:1px solid black;\n"
"border-radius:7px;\n"
"background:white;\n"
"color:rgb(70,70,70)}")
        self.recordTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.recordTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.recordTable.setLineWidth(1)
        self.recordTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.recordTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.recordTable.setDragEnabled(False)
        self.recordTable.setAlternatingRowColors(False)
        self.recordTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.recordTable.setGridStyle(QtCore.Qt.SolidLine)
        self.recordTable.setCornerButtonEnabled(False)
        self.recordTable.setObjectName("recordTable")
        self.recordTable.setColumnCount(2)
        self.recordTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recordTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recordTable.setHorizontalHeaderItem(1, item)
        self.recordTable.horizontalHeader().setCascadingSectionResizes(True)
        self.recordTable.horizontalHeader().setDefaultSectionSize(80)
        self.recordTable.horizontalHeader().setMinimumSectionSize(20)
        self.recordTable.horizontalHeader().setStretchLastSection(True)
        self.backButton_4 = QtWidgets.QPushButton(self.page_4)
        self.backButton_4.setGeometry(QtCore.QRect(10, 5, 25, 25))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backButton_4.setFont(font)
        self.backButton_4.setStyleSheet("QPushButton::pressed{\n"
"color:rgb(70,70,70);\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background-color:white}\n"
"QPushButton{color:white;\n"
"border:2px solid white;\n"
"border-radius :12px;\n"
"background:transparent}")
        self.backButton_4.setObjectName("backButton_4")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enrollButton.setText(_translate("MainWindow", "단어 등록하기"))
        self.memorizeButton.setText(_translate("MainWindow", "단어 외우기"))
        self.gameButton.setText(_translate("MainWindow", "게임하기"))
        self.recordButton.setText(_translate("MainWindow", "기록보기"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "단어"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "뜻"))
        self.enterButton_1.setText(_translate("MainWindow", "입력"))
        self.KorEdit.setText(_translate("MainWindow", "뜻"))
        self.EngEdit.setText(_translate("MainWindow", "단어"))
        self.backButton_1.setText(_translate("MainWindow", "<"))
        self.status_2.setText(_translate("MainWindow", "00/00"))
        self.wordScreen_2.setText(_translate("MainWindow", "eng"))
        self.backButton_2.setText(_translate("MainWindow", "<"))
        self.prev_2.setText(_translate("MainWindow", "<"))
        self.next_2.setText(_translate("MainWindow", ">"))
        self.score.setText(_translate("MainWindow", "0000점"))
        self.wordScreen_3.setText(_translate("MainWindow", "eng"))
        self.status_3.setText(_translate("MainWindow", "(00/00)"))
        self.backButton_3.setText(_translate("MainWindow", "<"))
        self.enterButton_3.setText(_translate("MainWindow", "입력"))
        item = self.recordTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "점수"))
        item = self.recordTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "날짜"))
        self.backButton_4.setText(_translate("MainWindow", "<"))

import resources_rc
