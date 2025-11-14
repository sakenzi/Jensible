from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QApplication,
    QWidget,
    QLabel,
    QSizePolicy,
    QLineEdit,
)
from PyQt5.QtCore import (
    QPersistentModelIndex,
)
from PyQt5.QtGui import (
    QPixmap,
)
import sys
import os
from resources.styles.auth_register_components import Styles
from resources.icons.auth_register_icons import ICONS


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class AuthRegisterWindow(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        self._setup_window()

    def _setup_window(self):
        self.setWindowTitle("Jensible (Register)")
        self.setGeometry(700, 400, 1500, 1000)
        self.setStyleSheet(Styles['auth_window'])

    