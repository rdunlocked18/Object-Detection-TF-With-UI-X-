import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton ,QLineEdit,QLabel,QMessageBox
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 500))
        self.setWindowTitle("Real Time Object Detection Using Tensorflow")


        self.textbox = QLineEdit(self)
        self.textbox.move(100, 50)
        self.textbox.resize(300, 50)

        self.button1 = QPushButton('Set Directory', self)
        self.button2 = QPushButton('Object Detection Using Local Photos', self)
        self.button3 = QPushButton('Object Detection Accuracy', self)
        self.button4 = QPushButton('Object Detection Real Time Webcam', self)
        self.button5 = QPushButton('Object Detection With Audio', self)
        self.button1.move(100, 150)
        self.button2.move(100, 200)
        self.button3.move(100, 250)
        self.button4.move(100, 300)
        self.button5.move(100, 350)
        self.button1.clicked.connect(self.directorymain)
        self.button2.clicked.connect(self.localPhotos)
        self.button3.clicked.connect(self.localPhotosAccuracy)
        self.button4.clicked.connect(self.webcampy)
        self.button5.clicked.connect(self.audio_det)


        #resize
        self.button1.resize(300, 50)
        self.button2.resize(300, 50)
        self.button3.resize(300, 50)
        self.button4.resize(300, 50)
        self.button5.resize(300, 50)
        #
        #
        # pybutton = QPushButton('Jailbreak Checkm8 X', self)
        # pybutton.clicked.connect(self.jailbreakme)
        # pybutton.resize(200, 32)
        # pybutton.move(50, 100)
        # pybutton.setToolTip('Click here to jailbreak')

        # change to the jailbreak main directory to checkm8
    def localPhotos(self):
        os.system('python localPhotosOnly.py')
    def localPhotosAccuracy(self):
        os.system('python object_detection_accuracy.py')
    def webcampy(self):
        os.system('python object_detection_webcam.py')
    def audio_det(self):
        os.system('python audio_detect.py')    

    def directorymain(self):
        try:
            pathToDirectory = self.textbox.text()
            os.chdir(pathToDirectory)
            print("Your Chosen Directory is : " ,pathToDirectory)
        except OSError as e:
         print(e.errno)
         
              ######### completey jailbreak via button click ###########

    # def jailbreakme(self):
        # directoryres = "/Users/rdunlocked/Desktop/Jailbreak/dfu" #/Users/rdunlocked/Desktop/Jailbreak/dfu
        # cmd2 = "./ipwndfu -p"
        # maincode = os.system(cmd2)
        # QMessageBox.question(self, 'Jailbreak Status !! ', "Jailbreak Timeout\n after 5 seconds : NO DFU Device", QMessageBox.Ok,
        #                      QMessageBox.Ok)
        # print('jailbreak status : ',maincode)


    # def accuracy(self):


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
