import sys
import os
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import success_window_gui as success_gui

class mind_id(QtWidgets.QMainWindow):
    def __init__(self):
        super(mind_id,self).__init__()
        self.dirname = os.path.dirname(__file__)
        filename = os.path.join(self.dirname, 'login_window.ui')
        # print (dirname)
        loadUi(filename, self)

        filename = os.path.join(self.dirname, 'background.png')
        self.label_2.setPixmap(QtGui.QPixmap(filename))

        #######################
        #### MY CODE STARTS HERE

        self.reset()
        
        self.login_b.clicked.connect(self.login_clicked)
        self.signup_b.clicked.connect(self.signup_clicked)
        self.verify.clicked.connect(self.verify_clicked)
        self.submit.clicked.connect(self.submit_clicked)
        self.browse.clicked.connect(self.browse_clicked)
        self.home_button.clicked.connect(self.home_clicked)
        self.verify_email.clicked.connect(self.verify_email_clicked)
        self.regex = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
        self.home_button_2.clicked.connect(self.home_clicked)


    def reset(self):
        self.home_button_2.setVisible(False)
        self.login_progress.setVisible(False)
        self.email_frame.setVisible(False)
        self.loginsignup_frame.setVisible(True)
        self.precess_frame.setVisible(False)
        self.username_frame.setVisible(False)
        self.edf_frame.setVisible(False)
        self.invalid_frame.setVisible(False)
        self.usname.clear()
        self.file_validity.clear()
        self.email.clear()
        self.file_path = ''
        self.status = ''

    def check_username(self):
        ## Check userName in database
        return False

    def validate_email(self, email):
        if(re.match(self.regex,email) != None):  
            return True  
        else:  
            return False

    def error_output(self, text):
        self.invalid_frame.setText(text)
        self.invalid_frame.setVisible(True)

    def verify_email_clicked(self):
        self.invalid_frame.setVisible(False)
        if (self.email.text()):
            if(self.validate_email(self.email.text())):
                self.email_frame.setVisible(False)
                self.email_id = self.email.text()
                self.line_edf.setText("SELECT ALL .edf FILES")
                self.edf_frame.setVisible(True)
            else:
                self.error_output("Invalid email ID")
        else:
            self.error_output("Please Enter email ID!")
    
    def home_clicked(self):
        self.reset()

    def start_process(self):
        self.loginsignup_frame.setVisible(False)
        self.precess_frame.setVisible(True)
        self.username_frame.setVisible(True)

    def login_clicked(self):
        self.status = 'login'
        self.progress_text.setText("ENTER           LOGIN           DETAILS")
        self.start_process()
        
    
    def signup_clicked(self):
        self.status = 'signup'
        self.progress_text.setText("ENTER           SIGNUP           DETAILS")
        self.start_process()
    
    def verify_clicked(self):
        if (self.usname.text()):
            self.user_name = self.usname.text()
            if (self.check_username()):
                self.usname.clear()
                if(self.status == 'login'):
                    # self.usname.clear()
                    self.invalid_frame.setVisible(False)
                    self.username_frame.setVisible(False)
                    self.edf_frame.setVisible(True)
                else:
                    self.error_output("Username already exist, try something else.")
            else:
                #print(self.usname.text())
                self.usname.clear()
                if(self.status == 'login'):
                    self.error_output("Invalid User! Please enter a valid Username.")
                else:
                    # self.usname.clear()
                    self.invalid_frame.setVisible(False)
                    self.username_frame.setVisible(False)
                    self.email_frame.setVisible(True)
        else:
            self.error_output("Please Enter a Username!")


    def check_file_format(self, file_path):
        file_path = file_path[-4:]
        if (file_path == '.edf' or file_path == '.EDF'):
            return True
        else:
            return False

    def login_successful(self):
        self.success_window = success_gui.login_successful()
        self.success_window.show()
        self.login_progress.setText("Login Successful!")


    def login_failed(self):
        self.login_progress.setText("Login failed!")
        self.home_button_2.setVisible(True)

    def signup_result(self, text):
        msg = 'signup ' + text
        self.login_progress.setText(msg)
        self.home_button_2.setVisible(True)

    def in_progress(self, text):
        self.reset()
        self.loginsignup_frame.setVisible(False)
        self.login_progress.setText(text)
        self.login_progress.setVisible(True)

    def submit_clicked(self):
        self.invalid_frame.setVisible(False)
        if (self.status == 'login'):
            if(len(self.file_path) > 0):
                if(self.check_file_format(self.file_path)):
                    self.in_progress("Login in Progress...")
                    # call predict function
                    predict = True
                    if (predict):
                        self.login_successful()
                    else:
                        self.login_failed()
                else:
                    self.error_output("Invalid file format!")
                    self.file_validity.clear()
            else:
                self.error_output("Please choose a file!")
        else:
            if(len(self.file_path) > 4):
                try:
                    for file_name in self.file_path:
                        assert(self.check_file_format(file_name))
                    self.in_progress("Signup in progress...")
                    ## call register function
                    register = True
                    if(register):
                        self.signup_result("successful!")
                    else:
                        self.signup_result("failed!")
                except:
                    self.error_output("Invalid file format!")
                    self.file_validity.clear()
            else:
                self.error_output("Select atlease 5 files")
                

    def browse_clicked(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        if(self.status == 'login'):
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
            if fileName:
                self.file_validity.setText(fileName)
                self.file_path = fileName
                # print(type(fileName))
                # print(fileName)
                # print(len(self.file_path))
        else:
            fileNames, _ = QtWidgets.QFileDialog.getOpenFileNames(None,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
            # print(type(fileNames))
            if (len(fileNames)>0):
                self.file_path = fileNames
                msg = str(len(fileNames)) + ' Files selected.'
                self.file_validity.setText(msg)


        
        #### MY CODE STARTS HERE
        #######################
