import sys
import os
import random
import numpy as np

from app.const.app_const import KeypointConst
from app.model.body_parts import ImageSize, Keypoint, ImageData
from app.utils.utils import creat_unique_id
from app.model.bll_i import BussinesLogicLayer
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow
from win32api import GetSystemMetrics

class MainWindowController:
    
    def __init__(self, model: BussinesLogicLayer, view: QMainWindow):
        self.model = model
        self.side_selected = False
        self.view = view
        self.view.exit_button.clicked.connect(self.exit_button_clicked)
        self.view.browse_button.clicked.connect(self.browse_button_clicked)
        self.view.open_image_button.clicked.connect(self.open_image_button_clicked)
        self.view.save_button.clicked.connect(self.save_button_clicked)
        
        self.view.front_side_button.clicked.connect(self.front_side_button_clicked)
        self.view.back_side_button.clicked.connect(self.back_side_button_clicked)
        
        self.view.show()
    def front_side_button_clicked(self):
        self.positions = self.model.get_positions(KeypointConst.IMAGE_DATA_FRONT)
        self.side_selected = True
    def back_side_button_clicked(self):
        self.positions = self.model.get_positions(KeypointConst.IMAGE_DATA_BACK)
        self.side_selected = True
    def browse_button_clicked(self):
        try:
            self.filename = self.view.open_file_dialog()
            self.img_stream = open(self.filename[0], 'rb')
            self.view.fileway.setText(self.filename[0])
        except NameError:
            self.browse_button_clicked()
        except FileNotFoundError:
            return
    
    def save_button_clicked(self):
        if hasattr(self, 'img') == False:
            self.view.raise_error_message("Please select an image!")
        else:
            img_size = ImageSize(self.img.shape[0], self.img.shape[1])
            img_id = creat_unique_id()
            keypoint_dict = self.model.list_to_dict(self.positions)
            image_data = ImageData(img_id, img_size, keypoint_dict, self.filename[0])
            self.model.insert_one_image_data(image_data)
            self.side_selected = False

    def open_image_button_clicked(self):
        if self.side_selected == False:
            self.view.raise_error_message("Please select a side!")
        else:
            self.img = self.get_img_from_file() 
            if self.img is None:
                return
            max_width = GetSystemMetrics(0)
            max_height = GetSystemMetrics(1)
            self.resize_img(max_width, max_height)
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
        try:
            img_bytes = bytearray(self.img_stream.read())
            img_np_array = np.asarray(img_bytes, dtype=np.uint8)
            img = cv2.imdecode(img_np_array, cv2.IMREAD_UNCHANGED)
            return img
        except AttributeError as e:
            self.view.raise_error_message("Please select an image!")  
            return None  
        except cv2.error as e:
            self.view.raise_error_message("Please select an image!")
            return None
        
    def resize_img(self, max_width, max_height):
        img_width, img_height,_ = self.img.shape
        while img_width > max_width or img_height > max_height:
            img_width = 50
            img_height += 50
        cv2.resize(self.img, (img_width, img_height))