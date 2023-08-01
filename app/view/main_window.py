from app.const.app_const import AppConst
from app.const.app_const import KeypointConst
import numpy as np
import cv2
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QFileDialog
#TODO: create fields for the constant ui values like thickness, color, etc.

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(AppConst.UI_PATH, self)

    def init_base_img(self, img):
        self.base_img = img
        
    #TODO: refactor this method
    def draw_skeloton(self, positions):        
        self.img = self.base_img.copy()
        for i in KeypointConst.EDGES:
            poly_lines = []
            for j in i:
                poly_lines.append(positions[j][:-1])
            draw_poly = np.array(poly_lines)
            cv2.polylines(self.img, [draw_poly], isClosed=False,
                          color=(0,255,0), thickness=2, lineType=cv2.LINE_4)
        for count1, pose in enumerate(positions):
            cv2.circle(self.img, center=(pose[0], pose[1]), radius=4, color=(
                (0,123,0)), thickness=-2, lineType=cv2.LINE_4)
            self.draw_skeloton_text(positions, count1)
            
    #TODO: refactor this method
    def draw_skeloton_text(self, positions, index):
        cv2.putText(self.img,
                        text=str([
                            keypoint_name
                            for keypoint_id, keypoint_name in enumerate(KeypointConst.IMAGE_DATA_FRONT.keypoints)
                            if keypoint_id == index][0]
                            ),           
                        org=(positions[index][0],
                             positions[index][1] - 10),
                        fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.75, color=(100, 100, 255),
                        thickness=2,
                        lineType=cv2.LINE_4)    
        
    def start_labeling(self, mouse_callback):
        cv2.namedWindow('labeling window', cv2.WINDOW_AUTOSIZE),
        cv2.setMouseCallback("labeling window", mouse_callback)
        while (1):
            cv2.imshow('labeling window', self.img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("s"):
                cv2.destroyAllWindows()
                break
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def open_file_dialog(self):
        return QFileDialog.getOpenFileName(self, 'Open file', AppConst.BASE_C_PATH,"Image files (*.jpg *.bmp)")