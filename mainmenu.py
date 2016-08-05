''''Module sine_plotter.py Name: Danna Useche fsuid:dcu13'''
import sys, os, random, subprocess
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QProcess



class MainMenuWindow(QtWidgets.QMainWindow):
    '''Full window'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        infoObject = app.desktop().screenGeometry()
        if((infoObject.width() >= 1920) and (infoObject.height() >= 950)):
            self.setGeometry(0, 32, 1000, 800)
            self.setFixedSize(1000, 800)
            self.backgroud = QtGui.QPalette()
            self.backgroud.setBrush(10, QtGui.QBrush(QtGui.QImage("menu_bg_1000.jpg")))
            self.setPalette(self.backgroud)
        else:
            self.setGeometry(0, 32, 800, 640)
            self.setFixedSize(800, 640)
            self.backgroud = QtGui.QPalette()
            self.backgroud.setBrush(10, QtGui.QBrush(QtGui.QImage("menu_bg_800.jpg")))
            self.setPalette(self.backgroud)
        self.setup()

    def setup(self):
        self.setWindowTitle('RMTD')
        self.menu = Menu(self)
        self.setCentralWidget(self.menu)


class Menu(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.setup()

    def setup(self):
        self.start_btn = StartBtn(self)
        self.quit_btn = QuitBtn(self)
        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(40, 260, 0, 220)
        self.combo = QtWidgets.QComboBox()
        self.combo.setFixedSize(150, 30)
        self.combo.addItems('Select-Level Level-One Level-Two Level-Three'.split())
        self.combo.currentIndexChanged.connect(self.level_selection)
        self.vbox.addWidget(self.start_btn)
        self.vbox.addWidget(self.combo)
        self.vbox.addWidget(self.quit_btn)
        self.start_btn.clicked.connect(self.on_start)
        #self.plot_btn.clicked.connect(self.on_plot)
        self.quit_btn.clicked.connect(QtWidgets.qApp.quit)

    def level_selection(self, i):
        print ("Current index %s" % (i))
        if(i == 1):
            cmd = 'python main.py grid.txt'
        elif(i == 2):
            cmd = 'python main.py map2.txt'
        elif (i == 3):
            cmd = 'python main.py map3.txt'
        self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    def on_start(self):
        cmd = 'python main.py grid.txt'
        self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)


    #def on_help(self):


class StartBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText('Start Game')
        self.setFixedSize(150, 30)

class HelpBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText('Help')
        self.setFixedSize(150, 30)

class QuitBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText('Quit')
        self.setFixedSize(150, 30)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainMenuWindow()
    main_window.show()
    app.exec_()
