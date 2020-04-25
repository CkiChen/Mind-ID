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
        self.background_2.setPixmap(QtGui.QPixmap(filename))

        ####################
        
        self.visualize_b.clicked.connect(self.visualize_b_clicked)
        self.home.clicked.connect(self.home_clicked)
        self.next_b.clicked.connect(self.next_clicked)
        self.perv_b.clicked.connect(self.prev_clicked)
        self.open_folder.clicked.connect(self.open_folder_clicked)
        self.index = 0

        #pushButton.clicked.connect(self.pushButton_clicked)

    def get_data(self):
        dirname = os.path.dirname(__file__)
        user = '../BackEnd/Res/Plots/' + str(self.user_name)
        path = os.path.join(dirname, user)
        self.names = ['Montage','raw data','raw epochs','power spectral density','epochs psd']
        filename1 = os.path.join(path, 'Montage.png')
        filename2 = os.path.join(path, 'raw-data.png')
        filename3 = os.path.join(path, 'raw_epochs.png')
        filename4 = os.path.join(path, 'power_spectral_density.png')
        filename5 = os.path.join(path, 'epochs_psd.png')
        self.images = [filename1, filename2, filename3, filename4, filename5]
    
    def open_folder_clicked(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, '../BackEnd/Res/Plots/')
        path = path + str(self.user_name)
        os.startfile(path)

    def visualize_b_clicked(self):
        # os.system('explorer.exe "C:\users\%username%\Desktop"')
        self.get_data()
        img = self.images[self.index]
        self.image_place_holder.setPixmap(QtGui.QPixmap(img))
        self.set_file_name()
        self.stackedWidget.setCurrentIndex(1)

    def set_file_name(self):
        name = self.names[self.index]
        self.file_name.setText(name)

    def home_clicked(self):
        self.index = 0
        self.stackedWidget.setCurrentIndex(0)
    
    def next_clicked(self):
        self.index = self.index + 1
        if (self.index > 4):
            return
        img = self.images[self.index]
        self.image_place_holder.setPixmap(QtGui.QPixmap(img))
        self.set_file_name()

    def prev_clicked(self):
        self.index = self.index - 1
        if (self.index < 0):
            return
        img = self.images[self.index]
        self.image_place_holder.setPixmap(QtGui.QPixmap(img))
        self.set_file_name()

    def set_user_name(self, user_name):
        self.user_name = user_name

        ####################

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = login_successful()
#     window.show()
#     sys.exit(app.exec_())

