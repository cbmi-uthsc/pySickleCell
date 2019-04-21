import sys
from PyQt4 import QtGui, QtCore
import os

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(150, 150, 900, 700)
        self.setWindowTitle("PySickleCell")
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        l1=QtGui.QLabel(self)
        QtGui.QLabel.minimumSizeHint(l1)
        l1.setText("Upload a csv file containing patient history and get your results in results Tab!")
        l1.move(500,20)
        l1.setGeometry(QtCore.QRect(30, 80, 830, 100))
        l1.setFont(QtGui.QFont('SansSerif', 16))

        extractAction = QtGui.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtGui.QAction("Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        history = QtGui.QAction("History", self)
        history.setShortcut("Ctrl+H")
        history.setStatusTip('show patient history')
        #history.triggered.connect()

        result = QtGui.QAction("Result", self)
        result.setShortcut("Ctrl+R")
        result.setStatusTip('show patient history')

        self.statusBar()

        pic = QtGui.QLabel(self)
        pic.setGeometry(23, 160, 1050, 330)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/process.png"))

        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(extractAction)

        hist = mainMenu.addMenu("History")
        res = mainMenu.addMenu("Results")

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(200,550)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(427, 480, 250, 20)

        self.btn = QtGui.QPushButton("Upload",self)
        self.btn.move(500,550)
        self.btn.clicked.connect(self.file_open)
        self.show()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        path=os.getcwd()+"input_file.csv"
        inp=open(path,'w')
        inp.write(file.read())
        file.close()
        inp.close()
        self.download()

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'r')
        path=os.getcwd()+"/input_file.csv"
        inp=open(path,'w')
        inp.write(file.read())
        
        file.close()
        inp.close()

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

        #self.l2=QtGui.QLabel(self)
        #QtGui.QLabel.minimumSizeHint(self.l2)
        #self.l2.setText("Upload successful")
        #self.l2.move(450,450)
        #self.l2.setGeometry(QtCore.QRect(0, 0, 100, 10))
        
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Quit',
                                            "Do you really want to exit the application?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Application closed")
            sys.exit()
        else:
            pass
        
  
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
