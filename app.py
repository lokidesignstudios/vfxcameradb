import os
import sys
import yaml

import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore

curr_dir = os.path.dirname(os.path.abspath(__file__))
cam_configs = os.listdir(os.path.join(curr_dir, 'config'))


class CameraDBUI(QtWidgets.QWidget):
    def __init__(self):
        super(CameraDBUI, self).__init__()
        self.setWindowTitle('Camera Database')
        self.setMinimumWidth(650)
        self.setMinimumHeight(200)
        self.create_widgets()
        self.create_layout()
        self.get_brands()

    def create_widgets(self):
        self.brand_lbl = QtWidgets.QLabel('Brand')
        self.brand_cmb = QtWidgets.QComboBox()
        self.cam_model_lbl = QtWidgets.QLabel('Camera Model')
        self.sensor_type_lbl = QtWidgets.QLabel('Sensor Type')
        self.sensor_type_le = QtWidgets.QLineEdit()
        self.sensor_type_le.setDisabled(True)
        self.camera_model_cmb = QtWidgets.QComboBox()
        self.resolution_lbl = QtWidgets.QLabel('Resolution')
        self.resolution_lst = QtWidgets.QListWidget()
        self.cam_name_lbl = QtWidgets.QLabel('Camera Name')

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(main_layout)

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.brand_lbl)
        h_box1.addWidget(self.brand_cmb)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.cam_model_lbl)
        h_box2.addWidget(self.camera_model_cmb)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.sensor_type_lbl)
        h_box3.addWidget(self.sensor_type_le)

        h_box4 = QtWidgets.QHBoxLayout()
        self.resolution_lbl.setAlignment(QtCore.Qt.AlignTop)
        h_box4.addWidget(self.resolution_lbl)
        h_box4.addWidget(self.resolution_lst)

        main_layout.addLayout(h_box1)
        main_layout.addLayout(h_box2)
        main_layout.addLayout(h_box3)
        main_layout.addLayout(h_box4)

        # Connections
        self.brand_cmb.currentIndexChanged.connect(self.get_camera)
        self.camera_model_cmb.currentIndexChanged.connect(self.get_dimensions)

    def get_brands(self):
        brands = [os.path.splitext(x)[0].capitalize() for x in cam_configs]
        self.brand_cmb.clear()
        self.brand_cmb.addItems(brands)

    def get_camera(self):
        config = self.get_config()
        cam_models = [x for x in config]
        self.camera_model_cmb.clear()
        self.camera_model_cmb.addItems(cam_models)
        self.get_dimensions()

    def get_dimensions(self):
        config = self.get_config()
        camera = self.camera_model_cmb.currentText()
        try:
            dimensions = config[camera]['dimension']
            sensor_type = config[camera]['sensor_type']
            self.resolution_lst.clear()
            self.resolution_lst.addItems(dimensions)
            self.sensor_type_le.setText(sensor_type)
        except KeyError as e:
            print('Key Not Found !!!', e)

    def get_config(self):
        path = os.path.join(curr_dir, 'config', self.brand_cmb.currentText().lower() + '.yaml')
        with open(path, 'r') as _file:
            config = yaml.load(_file, Loader=yaml.FullLoader)
            return config

    def create_camera(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    camdbui = CameraDBUI()
    camdbui.show()
    sys.exit(app.exec_())
