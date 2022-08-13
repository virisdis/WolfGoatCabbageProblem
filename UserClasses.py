

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget
from PyQt6.QtSvgWidgets import QSvgWidget




class Creature(QSvgWidget):


    def __init__(self, imagePath, initXpos, initYpos, mainWindow):
        super().__init__(imagePath, mainWindow)
        self.initXpos = initXpos
        self.initYpos = initYpos
        iconXsize = 100
        iconYsize = 100
        self.setGeometry(initXpos, initYpos, iconXsize, iconYsize)
        self.state = False


    def changeState(self):
        self.state = (self.state == False) # if False then True and vice versa
        self.check()

    def toDefaultState(self):
        if (self.state == True):
            self.changeState()
            self.check()


    def check(self):
        if (self.state == False):
            self.move(self.initXpos, self.initYpos)
        else:
            self.move(self.initXpos, self.initYpos - self.parent().height()//2)




class Farmer(Creature):
    signalFarmerStateIsFalse = pyqtSignal()
    signalFarmerStateIsTrue = pyqtSignal()


    def __init__(self, imagePath, initXpos, initYpos, mainWindow):
        super().__init__(imagePath, initXpos, initYpos, mainWindow)


    def slotToFarmer(self):
        creatureSender = self.sender()

        if (self.state == False):
            self.signalFarmerStateIsFalse.connect(creatureSender.slotFarmerStateIsFalse)
            self.signalFarmerStateIsFalse.emit()
            self.signalFarmerStateIsFalse.disconnect()
        elif (self.state == True):
            self.signalFarmerStateIsTrue.connect(creatureSender.slotFarmerStateIsTrue)
            self.signalFarmerStateIsTrue.emit()
            self.signalFarmerStateIsTrue.disconnect()

        self.changeState()




class Cargo(Creature):
    signalToFarmer = pyqtSignal()


    def __init__(self, imagePath, initXpos, initYpos, mainWindow):
        super().__init__(imagePath, initXpos, initYpos, mainWindow)


    def mousePressEvent(self, event):
        self.signalToFarmer.emit()


    def slotFarmerStateIsFalse(self):
        farmerSender = self.sender()
        if (self.state == False):
            self.changeState()
        else:
            pass


    def slotFarmerStateIsTrue(self):
        farmerSender = self.sender()
        if (self.state == True):
            self.changeState()
        else:
            pass
