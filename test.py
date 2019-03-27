import PyQt5 as qt
from PyQt5 import QtWidgets, QtCore
from gui import *

from random import shuffle
import operator
from datetime import datetime

words = {}
records = {}

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
        self.ui.next_2.pressed.connect(lambda : self.changeWord('next'))
        self.ui.prev_2.pressed.connect(lambda : self.changeWord('prev'))
        self.ui.wordScreen_2.pressed.connect(self.toggleWord)
        
    def reset(self):
        self.orderedEngs = list(words.keys())
        self.wordCount = len(self.orderedEngs)
        self.curNum = 0
        self.curEng = self.orderedEngs[0]
        self.changeWord('next')

    def changeWord(self, button):
        if button == 'next':
            if self.curNum <= self.wordCount-1:
                self.curEng = self.orderedEngs[self.curNum]
                self.ui.wordScreen_2.setText(self.curEng)
                self.ui.status_2.setText(str(self.curNum+1)+'/'+str(self.wordCount))
                self.curNum+=1
        else :
            if self.curNum >1:
                self.curEng = self.orderedEngs[self.curNum-2]
                self.ui.wordScreen_2.setText(self.curEng)
                self.curNum-=1
                self.ui.status_2.setText(str(self.curNum)+'/'+str(self.wordCount))

    def toggleWord(self):
        if self.ui.wordScreen_2.text() == self.curEng:
            self.ui.wordScreen_2.setText(words[self.orderedEngs[self.curNum-1]])
        else:
            self.ui.wordScreen_2.setText(self.orderedEngs[self.curNum-1])


class Game():
    def __init__(self, ui):
        self.ui = ui
        self.ui.enterButton_3.clicked.connect(self.checkWord)

    def reset(self):
        self.curEng =''
        self.curKor =''
        self.wrongs = []
        
        self.comboCount = 0
        self.score = 0
        
        self.curNum = 0
        self.wordCount = len(words)
        self.gen = self.wordGenerator(words)
        self.ui.score.setText(str(self.score)+'점')
        self.ui.answerEdit.clear()
        self.changeWord()

    def wordGenerator(self, words):
        keys = list(words.keys())
        shuffle(keys)
        for eng in keys:
            yield eng

    def checkWord(self):
        userAnswer = self.ui.answerEdit.text().strip()
        if userAnswer == words[self.curEng]:
            self.score += 5
            self.comboCount +=2
            self.ui.score.setText(str(self.score)+'점')
        else:
            self.wrongs.append(self.curEng)
        
        if self.comboCount > 1:
            self.ui.combo.setText('COMBO\n+10')
            self.comboAnim()
            self.comboCount = 0
            print('no')
            self.ui.combo.setText('')
        self.ui.answerEdit.clear()
        
        if self.curNum <= self.wordCount-1:
            self.changeWord()
        else:
            wrongWords = [wrong+':'+words[wrong] for wrong in self.wrongs]
            alert(str(self.score)+'점입니다.\n-------------\n'+'\n'.join(wrongWords))
            records[datetime.now().strftime('%m-%d(%H:%M:%S)')] = self.score
            self.reset()


    def changeWord(self):
        self.curEng = next(self.gen)
        self.curKor = words[self.curEng]
        self.ui.wordScreen_3.setText(self.curEng)
        self.ui.status_3.setText('('+str(self.curNum+1)+'/'+str(self.wordCount)+')')
        self.curNum+=1

    def comboAnim(self):
        print(self.ui.combo.text())
        self.anim = QtCore.QPropertyAnimation(self.ui.combo, b"geometry")
        self.anim.setDuration(150)
        self.anim.setStartValue(QtCore.QRect(215, 25, 71, 41))
        self.anim.setEndValue(QtCore.QRect(220, 20, 71, 41))
        self.anim.start()
        print('done')


class Record:

    def __init__(self, ui):
        self.ui = ui
    
    def showRecord(self):
        print(records)
        if records:
            while self.ui.recordTable.rowCount() > 0:
                self.ui.recordTable.removeRow(0)
            self.record = sorted(records.items(), key=operator.itemgetter(1))
            for r in self.record:
                rowPosition = self.ui.recordTable.rowCount()
                self.ui.recordTable.insertRow(rowPosition)
                self.ui.recordTable.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(r[1])))
                self.ui.recordTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(r[0]))



class WordMaster(Enroll, Memorize, Game, Record):
    def __init__(self, ui):
        self.readWords()
        self.readRecords()
        self.enroll = Enroll(ui)
        self.memorize = Memorize(ui)
        self.game = Game(ui)
        self.record = Record(ui)
        ui.enrollButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(1))
        ui.memorizeButton.clicked.connect(self.memorize.reset)
        ui.memorizeButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(2))
        ui.gameButton.clicked.connect(self.game.reset)
        ui.gameButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(3))

        backButtonList = [ui.backButton_1, ui.backButton_2, ui.backButton_3, ui.backButton_4]
        for backButton in backButtonList:
            backButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(0))
        ui.recordButton.clicked.connect(self.record.showRecord)
        ui.recordButton.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(4))

    def readRecords(self):
        with open(r'records.txt', 'r', encoding='utf8') as t:
            while True:
                line = t.readline()
                if line:
                    time, score = line.strip().split()
                    records[time] = int(score)
                else:
                    break

    
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

    def saveRecord(self):
        with open(r'records.txt','a', encoding='utf8') as t:
            for time, score in records.items():
                t.write(time+' '+str(score)+'\n')

    def quit(self):
        self.saveWords()
        self.saveRecord()


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