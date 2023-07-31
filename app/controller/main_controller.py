import sys
import os

import numpy as np
from app.model.keypoint_repo_i import KeypointRepository
from app.model.json_repo import JsonRepo
from app.view.tool_ui import MainWindow
from app.const.app_const import AppConst

import cv2
from PyQt5.QtWidgets import QApplication, QFileDialog
from win32api import GetSystemMetrics

class MainWindowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.exit_button.clicked.connect(self.exit_button_clicked)
        self.view.browse_button.clicked.connect(self.browse_button_clicked)
        self.view.open_image_button.clicked.connect(self.open_image_button_clicked)
        self.view.show()
    def browse_button_clicked(self):
        try:
            filename = QFileDialog.getOpenFileName(self.view, 'Open file', AppConst.BASE_C_PATH,"Image files (*.jpg *.bmp)")
            self.img_stream = open(filename[0], 'rb')
            self.view.fileway.setText(filename[0])
        except NameError:
            self.browse_button_clicked()
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.file} not found')
        
    def save_button_clicked(self):
        raise NotImplementedError
    
    
    def open_image_button_clicked(self):      
        self.img = self.get_img_from_file()
        max_width = GetSystemMetrics(0)
        max_height = GetSystemMetrics(1)
        self.resize_img(max_width, max_height)
        
        self.check = False
        self.left_click = None
        cv2.namedWindow('labeling window', cv2.WINDOW_AUTOSIZE),
        cv2.setMouseCallback("labeling window", self.mouse_callback)
        cv2.imshow('labeling window', self.img)
        
    def exit_button_clicked(self):
        QApplication.quit()
    
    def mouse_callback(self, event, x, y, flags, param):
        raise NotImplementedError
        
    
    def get_img_from_file(self):
        img_bytes = bytearray(self.img_stream.read())
        img_np_array = np.asarray(img_bytes, dtype=np.uint8)
        img = cv2.imdecode(img_np_array, cv2.IMREAD_UNCHANGED)
        return img
    
    def resize_img(self, max_width, max_height):
        img_width, img_height,_ = self.img.shape
        while img_width > max_width or img_height > max_height:
            img_width -= 50
            img_height -= 50
        cv2.resize(self.img, (img_width, img_height))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    model = JsonRepo("app\resources\test.json")
    view = MainWindow()
    controller = MainWindowController(model, view)
    sys.exit(app.exec_())
