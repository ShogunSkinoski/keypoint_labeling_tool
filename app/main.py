from PyQt5.QtWidgets import QApplication
from app.controller.main_controller import MainWindowController
from app.model.json_repo import JsonRepo
from app.model.labelling_bll import LabelingBussinesModel
from app.view.main_window import MainWindow

import sys        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    model = LabelingBussinesModel(JsonRepo("app/resources/test.json"))
    view = MainWindow()
    controller = MainWindowController(model, view)
    sys.exit(app.exec_())