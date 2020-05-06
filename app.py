import os
import sys
import yaml

import PySide2.QtWidgets as QtWidgets

curr_dir = os.path.dirname(os.path.abspath(__file__))
cam_configs = os.listdir(os.path.join(curr_dir, 'config'))


def get_config(path):
    with open(path, 'r') as _file:
        config = yaml.load(_file, Loader=yaml.FullLoader)
        print(config)
        return config


class CameraDBUI(QtWidgets.QWidget):
    def __init__(self):
        super(CameraDBUI, self).__init__()
        self.setWindowTitle('Camera Database')
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.brand_lbl = QtWidgets.QLabel('Brand')
        self.cam_model_lbl = QtWidgets.QLabel('Camera Model')
        self.resolution_lbl = QtWidgets.QLabel('Resolution')

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.brand_lbl)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.cam_model_lbl)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.resolution_lbl)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    camdbui = CameraDBUI()
    camdbui.show()
    sys.exit(app.exec_())
