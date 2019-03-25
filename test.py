import PyQt5 as qt
from PyQt5 import QtWidgets
from gui import *

words = {}

def alert(message):
    if message:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        subapp = msgBox.exec_()

class Enroll:

    def __init__(self, ui):
        self.ui = ui
        self.ui.enterButton_1.clicked.connect(self.enrollWords)
        self.viewWords()

    def viewWords(self):
        for eng, kor in words.items():
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(eng))
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(kor))
    
    def enrollWords(self):
        eng = self.ui.EngEdit.text()
        kor = self.ui.KorEdit.text()        
        if not(eng and kor):
            alert("단어를 입력해주십시오.")
        elif not words.get(eng) == kor:
            words[eng] = kor
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(eng))
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(kor))
        else:
            alert("이미 등록된 단어입니다.")
        self.ui.EngEdit.clear()
        self.ui.KorEdit.clear()

class Memorize:
    def __init__(self, ui):
        self.ui = ui
        self.ui.word_2.clicked.connect(lambda x: ui.word_2.setText(
            words[ui.word_2.text()] if ui.word_2.text().isalpha() else words.) )
        self.ui.next_2.clicked.connect(self.showWord('next'))
        self.ui.next_3.clicked.connect(self.showWord('prev'))

    def showWord(self, button):
        if button == 'next':
        else :

            


class Game:
    def __init__(self, ui):
        pass
        #self.readWords()
        #ui.pushbutton.clicked.connect(lambda : 
        #    ui.score.setText(int(ui.score.text())+10) if words[ui.pushButton_2.text()] == ui.lineEdit.text())

    #def showWord(self):
    #    ui.pushButton_2.setText()


class Record:
    def __init__(self, ui):
        pass



class WordMaster(Enroll, Memorize, Game, Record):
    def __init__(self, ui):
        self.readWords()
        self.enroll = Enroll(ui)
        self.memorize = Memorize(ui)
        self.game = Game(ui)
        self.Record = Record(ui)
        ui.enrollButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(1))
        ui.memorizeButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(2))
        ui.gameButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(3))

        backButtonList = [ui.backButton_1, ui.backButton_2, ui.backButton_3]
        for backButton in backButtonList:
            backButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(0))
        #ui.recordButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(4))

        
        print('ok')
    
    def readWords(self):
        with open(r'words.txt','r', encoding='utf8') as t:
            while True:
                line = t.readline()
                if line:
                    eng, kor = line.strip().split()
                    words[eng] = kor
                else:
                    break

    def saveWords(self):
        with open(r'words.txt', 'w', encoding = 'utf8') as t:
            for eng, kor in words.items():
                t.write(eng+' '+kor+'\n')

    def quit(self):
        self.saveWords()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.showFullScreen()
    wordMaster = WordMaster(ui)
    MainWindow.show()
    app.aboutToQuit.connect(wordMaster.quit)
    sys.exit(app.exec_())