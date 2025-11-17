from PyQt5.QtWidgets import (
    QWidget, 
    QApplication, 
    QMainWindow, 
    QVBoxLayout, 
    QHBoxLayout,
    QPushButton, 
    QComboBox, 
    QLineEdit, 
    QAction, 
    QLabel, 
    QMenu,
)
from PyQt5.QtCore import (
    QSize, 
    QTimer,
)
from PyQt5.QtGui import (
    QIcon,
)
import sys
import os
from resources.styles.main_components import Styles


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class MainWindow(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager()
        self._setup_window()

    def _setup_window(self):
        self.setWindowTitle("Jensible (Main Window)")
        self.setGeometry(250, 200, 1500, 1000)
        self.setStyleSheet(Styles["main_window"])

    