# TicTacToe-Game-Python


from PySide6.QtWidgets import *
from PySide6.QtGui import*
import random
from newWindow import *

w=600
h=600
allbtns=[]
list=[]
xPos=0
yPos=0
light=True
clickCount=0
xCount=0
app=QApplication()

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentWindow=None
        self.resize(600,600)
        self.button=btn     
        

    def newwin(self):
        self.currentWindow=secondWind()
        self.currentWindow.show()

    def conditions(self):
        for i in allbtns:
            if self.coord['x']==1:
                if self.text()=='X':
                    self.newwin() 
        
        
        
class Tictacbtn(QPushButton):
    def __init__(self,*args):
        QPushButton.__init__(self,*args)
        self.clicked.connect(self.clickFunk)
        self.clickCount=0
        
        
        self.coord={
            'x':0,
            'y':0
        }
      
    def clickFunk(self):
        global clickCount
        global light,xCount
        self.clickCount+=1
        print(self.coord)
        if self.clickCount<=1:
            if light:
                self.setText('X')
                self.setStyleSheet('background-color:#79c2d0')
                light=False
            else:
                self.setText('O')
                self.setStyleSheet('background-color:#f70776')
                light=True
            

                
                                           
        
    def defineCoordinate(self,x,y):
        self.coord['x']=x
        self.coord['y']=y
    
for setir in range(3):
    for sutun in range(3):
        btn=Tictacbtn('',main)
        btn.setGeometry(xPos,yPos,w/3,h/3)
        btn.defineCoordinate(setir,sutun)
            
        allbtns.append(btn)
        
        
                                
        xPos+=200
    xPos=0   
    yPos+=200       
                                          



Main=main()
Main.show()
app.exec_()