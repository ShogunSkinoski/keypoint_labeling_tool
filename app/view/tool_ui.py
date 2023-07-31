from app.const.app_const import AppConst

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(AppConst.UI_PATH, self)