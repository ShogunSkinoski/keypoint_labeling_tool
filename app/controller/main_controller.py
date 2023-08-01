import sys
import os
import random
import numpy as np

from app.view.main_window import MainWindow
from app.const.app_const import KeypointConst
from app.model.json_repo import JsonRepo
from app.model.labelling_bll import LabelingBussinesModel
from app.model.bll_i import BussinesLogicLayer
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow
from win32api import GetSystemMetrics

class MainWindowController:
    
    def __init__(self, model: BussinesLogicLayer, view: QMainWindow):
        self.model = model

        self.view = view
        self.view.exit_button.clicked.connect(self.exit_button_clicked)
        self.view.browse_button.clicked.connect(self.browse_button_clicked)
        self.view.open_image_button.clicked.connect(self.open_image_button_clicked)
        
        self.positions = self.model.get_positions(KeypointConst.IMAGE_DATA_FRONT)
        
        self.view.show()
        
    def browse_button_clicked(self):
        try:
            filename = self.view.open_file_dialog()
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
        self.left_click = None
        self.check = False
        self.left_click = None
        self.view.init_base_img(self.img)
        self.view.draw_skeloton(self.positions)
        self.view.start_labeling(self.mouse_callback)
        
        
    def exit_button_clicked(self):
        QApplication.quit()
    
    
    def mouse_callback(self, event, x, y, flags, param):
        if self.left_click == True and flags == 0:
            self.view.draw_skeloton(self.positions)
            self.left_click = False
        if event == cv2.EVENT_MOUSEMOVE:
            if flags == 1 and self.check == False:
                self.left_click = True
                for index, keypoint in enumerate(self.positions):
                    if keypoint[0] - 10 < x < keypoint[0] + 10 and keypoint[1] - 10 < y < keypoint[1] + 10:
                        self.check = True
                        self.view.draw_skeloton_text(self.positions, index)
                        self.position_index = index
                        break
            elif flags == 1 and self.check == True:
                self.positions[self.position_index][0] = x
                self.positions[self.position_index][1] = y
                
            elif self.check == True and flags == 0:
                self.check = False  
        
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
    
    model = LabelingBussinesModel(JsonRepo("app\resources\test.json"))
    view = MainWindow()
    controller = MainWindowController(model, view)
    sys.exit(app.exec_())
