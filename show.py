import PyQt5.QtWidgets as qt
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect,QTimer,QSize
from PyQt5.QtCore import *
import sys
import time
import re
import codecs

#QDialog vs QMainWindow

class Window(qt.QMainWindow):
        def __init__(self):
                super().__init__()
                self.title = "國中單字▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ 各種場所的英文"
                self.icon = "home.png"
                self.timer = QTimer(self)

                self.count=0
                self.lines=[]
                
                self.InitWindow()
                
        def InitWindow(self):
                self.setWindowTitle(self.title)
                self.setWindowIcon(QtGui.QIcon("william.png"))
                #timer = QTimer()
                f = QtGui.QFont()
                f.setBold(True)
                f.setFamily("arial")
                f.setPointSize(100)

                
                """
                self.button = qt.QPushButton(" ",self)
                self.button.setIcon(QtGui.QIcon("william.png"))
                self.button.setStyleSheet("background-color:azure, text-align: center")
                self.button.setIconSize(QSize(100,100))
                self.button.setFont(f)
                self.button.setGeometry(QRect(5,0,2000,1020))
                """
                #vbox = qt.QVBoxLayout()
                
                filename = "場所.txt"
                self.process(filename)
                self.get_words("new_" + filename)
                
                self.eng = qt.QLabel(self.lines[self.count],self)
                self.eng.resize(1914,400)
                self.eng.move(0,250)
                self.eng.setAlignment(Qt.AlignCenter)
                self.chin = qt.QLabel(self.lines[self.count+1],self)
                self.chin.resize(1914,200)
                self.chin.move(0,600)
                self.chin.setAlignment(Qt.AlignCenter)
                #vbox.addWidget(self.eng)
                #vbox.addWidget(self.chin)
                #self.setLayout(vbox)
                
                self.show()

                self.timer.start(4000)
                self.timer.timeout.connect(self.show)    
                self.showMaximized()
                
                        
        def show(self):

                f_eng= QtGui.QFont()
                f_eng.setBold(True)
                f_eng.setFamily("papyrus")
                f_eng.setPointSize(150)

                f_chin= QtGui.QFont()
                f_chin.setBold(True)
                f_chin.setFamily("微軟正黑體")
                f_chin.setPointSize(90)
                if(self.count==len(self.lines)):
                        self.timer.stop()
                        return

                self.eng.setFont(f_eng)
                self.eng.setText(self.lines[self.count])

                self.chin.setFont(f_chin)
                self.chin.setText(self.lines[self.count+1])

                self.count = self.count+2

        def get_words(self,filename):
                f = open(filename, encoding="utf-8")
                line = f.readline().split()
                #print(line)
                while (len(line)>=2):
                        eng = line[0]
                        for i in range(2,len(line)):
                                eng = eng + " " + line[i-1]
                        chin = line[len(line)-1]
                        self.lines.append(eng)
                        self.lines.append(chin)
                        line = f.readline().split()
                print(self.lines)


        def process(self, filename,has_symbol=False):

                if has_symbol:
                        f = open(filename,encoding="utf-8")
                        file = open("new_" + filename, 'w+', encoding="utf-8")
                        count=0
                        for line in f.readlines():
                                chin=""
                                for i in range(len(line.split("@")[1])):
                                        if(re.search("\d+",line.split("@")[1][i])):
                                                continue
                                        else:
                                                if(line.split("@")[1][i]=="，" or line.split("@")[1][i]=="(" or line.split("@")[1][i]=="\n"):
                                                        break
                                                chin = chin + line.split("@")[1][i]
                                file.write(line.split("@")[0] + " ")
                                chin_word = chin + "\n"
                                file.write(chin_word)
                                count = count + 1
                        file.writelines(time.strftime("%Y%m%d",time.localtime()))
                        i = filename.find(".")
                        print("There are " + str(count)+ " kinds of " + filename[0:i])
                else:
                        f = open(filename, encoding="utf-8")
                        file = open("new_" + filename, 'w+', encoding="utf-8")
                        count=0
                        for line in f.readlines():
                                string=""
                                if(len(line.split()))>2:
                                        for i in range(len(line.split())):
                                                if(i==(len(line.split())-1)):
                                                        string = string + line.split()[i] + "\n"
                                                        break
                                                string = string + line.split()[i] + " "
                                        file.writelines(string)
                                else:
                                        file.writelines(line.split()[0] + " " + line.split()[1] + "\n")
                                count = count + 1
                        file.writelines(time.strftime("%Y%m%d",time.localtime()))
                        i = filename.find(".")
                        print("There are " + str(count)+ " kinds of " + filename[0:i])
                        
app = qt.QApplication([])
window = Window()
sys.exit(app.exec())

            
