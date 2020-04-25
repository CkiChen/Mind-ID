import sys
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'GUI/')
sys.path.append(filename)
from gui import *
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = mind_id()
	window.show()
	sys.exit(app.exec_())

