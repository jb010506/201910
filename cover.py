import PyQt5.QtWidgets as qt
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QColor   
from PyQt5.QtCore import QRect,QTimer,QSize
from PyQt5.QtCore import *
import sys
import time
import re

#QDialog vs QMainWindow

class Window(qt.QMainWindow):
        def __init__(self):
                super().__init__()
                self.title = "國中單字▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ 各種天氣與季節"
                self.icon = "home.png"
                self.timer = QTimer(self)

                self.count=0
                self.lines=[]
                
                self.InitWindow()
                
        def InitWindow(self):
                self.setWindowTitle(self.title)
                self.setWindowIcon(QtGui.QIcon("william.png"))
                p = self.palette()
                p.setColor(self.backgroundRole(),QColor(204,240,240))
                self.setPalette(p)

                f1 =QFont("微軟正黑體", 150,QFont.Bold)
                f2 =QFont("微軟正黑體", 150,QFont.Bold)



                #f2.setUnderline(True)
                self.label = qt.QLabel("國中單字", self)
                self.label.resize(1914,550)
                self.label.setFont(f1)
                self.label.setAlignment(Qt.AlignCenter)
                self.label.move(0,100)
                
                self.label2 = qt.QLabel("天氣與季節", self)
                self.label2.resize(1914,750)
                self.label2.setFont(f2)
                self.label2.setAlignment(Qt.AlignCenter)
                self.label2.move(0,300)
                self.label2.setStyleSheet("color:rgb(100,200,0)")


                self.showMaximized()
                        
        

            
app = qt.QApplication([])
window = Window()
sys.exit(app.exec())

            
