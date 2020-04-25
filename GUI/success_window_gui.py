import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class login_successful(QtWidgets.QMainWindow):
    def __init__(self):
        super(login_successful,self).__init__()
        self.dirname = os.path.dirname(__file__)
        filename = os.path.join(self.dirname, 'success_window.ui')
        # print (dirname)
        loadUi(filename, self)

        filename = os.path.join(self.dirname, 'success_window_background_1.jpg')
        self.background.setPixmap(QtGui.QPixmap(filename))

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = login_successful()
#     window.show()
#     sys.exit(app.exec_())

