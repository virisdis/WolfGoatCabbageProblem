

import sys, array
from PyQt6.QtCore import QSize, QObject, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtSvgWidgets import QSvgWidget

from UserClasses import Farmer, Cargo




class MainWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        windWidth = 800
        windLength = 600
        assert(windWidth % 2 == 0)
        assert(windLength % 2 == 0)

        self.setFixedSize(QSize(windWidth, windLength))
        self.setWindowTitle('Wolf, goat and cabbage: Boosting your right brain muscles')
        self.initLabel()
        self.initBackground()
        self.initCreatures()
        self.initButtons()
        self.show()


    def initLabel(self):
        self.label = QLabel(self)
        self.label.setText("<span style=\" font-size:20pt; font-weight:800;\">Let's take these creatures across the river</span>")
        self.label.move(100, 25)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)


    def initBackground(self):
        river = QSvgWidget('./images/river.svg', self)
        river.setGeometry(0,200,800,200)


    def initCreatures(self):

        initXpos = 50
        initYpos = 400
        self.farmer = Farmer('./images/farmer.svg', initXpos, initYpos, self)

        initXpos = 200
        self.wolf = Cargo('./images/wolf.svg', initXpos, initYpos, self)
        self.wolf.signalToFarmer.connect(self.farmer.slotToFarmer)

        initXpos = 400
        self.goat = Cargo('./images/goat.svg', initXpos, initYpos, self)
        self.goat.signalToFarmer.connect(self.farmer.slotToFarmer)

        initXpos = 600
        self.cabbage = Cargo('./images/cabbage.svg', initXpos, initYpos, self)
        self.cabbage.signalToFarmer.connect(self.farmer.slotToFarmer)

        self.creatures = [self.farmer, self.wolf, self.goat, self.cabbage]


    def initButtons(self):

        button1 = QPushButton('Roll back', self)
        button1.clicked.connect(self.button1Clicked)
        button1.setGeometry(0,550,400,50)

        button2 = QPushButton('Exit', self)
        button2.clicked.connect(self.button2Clicked)
        button2.setGeometry(400,550,400,50)


    def button1Clicked(self):

        for creature in self.creatures:
            creature.toDefaultState()

        self.label.setText("<span style=\" font-size:20pt; font-weight:800;\">Try one more time!</span>")
        print("Rolled back!")

        for creature in self.creatures:
            creature.setEnabled(1)


    def button2Clicked(self):
        print("The window has been closed.")
        self.close()


    def mouseReleaseEvent(self, event):

        if ((self.wolf.state == self.goat.state and self.farmer.state != self.wolf.state) or (self.goat.state == self.cabbage.state and self.farmer.state != self.goat.state)):
            self.label.setText("<span style=\" font-size:20pt; font-weight:800;\">GAME OVER!</span>")

            for creature in self.creatures:
                creature.setEnabled(0)


        if ((self.wolf.state == True) and (self.goat.state == True) and (self.cabbage.state == True) and (self.farmer.state == True)):
            self.label.setText("<span style=\" font-size:20pt; font-weight:800;\">VICTORY IS YOURS!</span>")

            for creature in self.creatures:
                creature.setEnabled(0)




app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
