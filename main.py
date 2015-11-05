# Information
__author__ = "Daniel Roland Henrik Jensen"
__copyright__ = "Copyright (C) 2015 Daniel Jensen"
__license__ = "Apache License 2.0, See the LICENSE file included"
__version__ = "1.0"

# Imports 
import sys
import random
import string
from PyQt4 import QtGui, QtCore


# The main window
class main_window(QtGui.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        
        # The position of main_window (500, 500) and the width and height (700, 500)
        self.setGeometry(500, 500, 700, 500)
        
        # The title of main_window
        self.setWindowTitle("Password Generator")
        
        # The icon of main_window
        self.setWindowIcon(QtGui.QIcon(''))

        # The minium width and height of main_window
        self.setMinimumSize(700, 500)

        # The maximum width and height of main_window 
        self.setMaximumSize(700, 500)

        # Where you decides how long your key is going to be
        self.le = QtGui.QLineEdit(self)
        self.le.move(200, 60)
        self.le.resize(self.le.sizeHint())

        # Where the random generated key goes
        self.txt_edit = QtGui.QTextEdit(self)
        self.txt_edit.move(200, 120)
        self.txt_edit.resize(self.txt_edit.sizeHint())

        self.home()

    def home(self):

        # Info label: txt_edit
        txt_label = QtGui.QLabel("Where your key(s) goes:", self)
        txt_label.move(10, 120)
        txt_label.resize(txt_label.sizeHint())

        # Generates the key
        g_button = QtGui.QPushButton("Generate", self)
        g_button.clicked.connect(self.length_check())
        g_button.resize(g_button.sizeHint())
        g_button.move(400, 60)

        # Info label: le
        label_le = QtGui.QLabel("Length of your key:", self)
        label_le.move(45, 60)
        label_le.resize(label_le.sizeHint())

        self.show()

    '''

        Insures that the password can get larger than 30 and less than 0.
        If the circumstances is right, it will print the generated key into the text edit(txt_edit in the home function)

    '''
    def length_check(self, *args):
        mytext = self.le.text()
        mytext_int = int(mytext)

        if mytext_int >= 31:
            QtGui.QMessageBox.information(self, "Not so many!", "Your password can't be higher than 30. If you want to"
                                                                " have a password that is higher than 30,"
                                                                " buy the full version.")

        if mytext_int <= 0:
            QtGui.QMessageBox.information(self, "Realy?", "Your password can't be less than one!")

        if mytext_int >= 1 or 31 >= mytext_int:
            self.txt_edit.append(generate_password(mytext_int))


# Generates a random key
def generate_password(y, yy=string.ascii_letters + string.digits):
    return ''.join(random.choice(yy) for x in range(y))


# The function that's running the application
def run():
    app = QtGui.QApplication(sys.argv)
    Gui = main_window()
    sys.exit(app.exec_())


run()
