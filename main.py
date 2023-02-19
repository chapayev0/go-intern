# -*- coding: utf-8 -*-
import sys
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from ui.ui_main import *
from ui.ui_login import *

import os

class login_ui(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_login()
        self.ui.setupUi(self)

class main_ui(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = login_ui()

    window.show()
    sys.exit(app.exec_())
