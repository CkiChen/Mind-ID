import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class trial_code(QtWidgets.QMainWindow):
    def __init__(self):
        super(trial_code,self).__init__()
        loadUi('login_window.ui', self)

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


    def reset(self):
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
        return True

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
                if(self.status == 'login'):
                    self.usname.clear()
                    self.invalid_frame.setVisible(False)
                    self.username_frame.setVisible(False)
                    self.edf_frame.setVisible(True)
                else:
                    self.error_output("Username already exist, try something else.")
            else:
                #print(self.usname.text())
                if(self.status == 'login'):
                    self.error_output("Invalid User! Please enter a valid Username.")
                else:
                    self.usname.clear()
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

    def submit_clicked(self):
        self.invalid_frame.setVisible(False)
        if (self.status == 'login'):
            if(len(self.file_path) > 0):
                if(self.check_file_format(self.file_path)):
                    # call predict function
                    pass
                else:
                    self.error_output("Invalid file format!")
            else:
                self.error_output("Please choose a file!")
        else:
            if(len(self.file_path) > 4):
                try:
                    for file_name in self.file_path:
                        assert(self.check_file_format(file_name))
                    ## call register function
                except:
                    self.error_output("Invalid file format!")
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



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = trial_code()
    window.show()
    sys.exit(app.exec_())
