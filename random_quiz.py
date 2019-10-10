import PyQt5.QtWidgets as qt
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect,QTimer,QSize
from PyQt5.QtCore import *
import sys
import time
import re

#QDialog vs QMainWindow

class Window(qt.QMainWindow):
        def __init__(self):
                super().__init__()
                self.title = "▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ 隨機單字測驗(1) ▉█ ▇ ▆ ▅ ▄ ▃ ▂ ▁"
                self.timer = QTimer(self)
                self.timer2 = QTimer(self)
                self.count=0
                self.time=0
                self.lines=[]
                
                self.InitWindow()
                
        def InitWindow(self):
                self.setWindowTitle(self.title)
                self.setWindowIcon(QtGui.QIcon("william.png"))

                
                #timer = QTimer()
                f = QtGui.QFont()
                f.setBold(True)
                f.setFamily("Adobe Garamond Pro")
                f.setPointSize(180)

                f2 = QtGui.QFont()
                f2.setBold(True)
                f2.setFamily("標楷體")
                f2.setPointSize(120)
                #f2.setUnderline(True)

                f3 = QtGui.QFont()
                f3.setBold(True)
                f3.setFamily("Chiller")
                f3.setPointSize(110)
                
                self.eng = qt.QLabel("",self)
                self.eng.resize(1914,350)
                self.eng.move(0,200)
                self.eng.setAlignment(Qt.AlignCenter)
                self.eng.setStyleSheet("color: rgb(102,102,255)")
                
                self.chin = qt.QLabel("",self)
                self.chin.resize(1914,200)
                self.chin.move(0,580)
                self.chin.setAlignment(Qt.AlignCenter)
                self.chin.setStyleSheet("color: rgb(64,64,64)")

                self.ans = qt.QLabel("",self)
                self.ans.resize(800,200)
                self.ans.move(200,600)
                self.ans.setText("Ans : ")
                self.ans.setFont(f3)
                self.ans.setStyleSheet("color: rgb(255,0,0)")

                self.underline = qt.QLabel("__________",self)
                self.underline.resize(800,200)
                self.underline.move(600,600)
                self.underline.setFont(f2)
                self.underline.setStyleSheet("color:rgb(96,96,96)")
                
                #vbox.addWidget(self.eng)
                #vbox.addWidget(self.chin)
                #self.setLayout(vbox)
                self.get_words()
                
                self.showMaximized()
                self.eng.setFont(f)
                self.chin.setFont(f2)
                self.eng.setText(self.lines[self.count])
                self.chin.setText("   "*len(self.lines[self.count+1]))
                self.timer.start(1000)
                self.timer.timeout.connect(self.up)
                
        def up(self):
                self.time = self.time + 1
                if(self.time==4):
                        self.chin.setText(self.lines[self.count+1])
                elif(self.time==6):
                        self.time=0
                        self.count = self.count + 2
                        if self.count==len(self.lines):
                                return
                        self.eng.setText(self.lines[self.count])
                        self.chin.setText("")
                        
                
        def answer(self):
                f_chin= QtGui.QFont()
                f_chin.setBold(True)
                f_chin.setFamily("微軟正黑體")
                f_chin.setPointSize(70)
                self.chin.setFont(f_chin)
                self.chin.setText(self.lines[self.count+1])
                self.count = self.count+2
                
        def get_words(self):
                f = open("C:\\Users\\william\\Desktop\\daily\\youtube\\隨機單字測驗\\quiz1.txt")
                line = f.readline().split(" ")
                while (not(line[0].startswith("#"))):
                        print(line)
                        self.lines.append(line[0])
                        self.lines.append(line[1])
                        line = f.readline().split(" ")
                print("There are " + str(len(self.lines)//2) + " exercises")
            
app = qt.QApplication([])
window = Window()
sys.exit(app.exec())

            
