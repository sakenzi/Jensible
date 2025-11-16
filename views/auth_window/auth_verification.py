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
from resources.styles.auth_login_components import Styles
from resources.images.auth_login_images.auth_login_images import IMAGE


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class AuthVerificationEmail:
    def __init__(self, app_manager):
        self.app_manager = app_manager
        self._setup_window()

    def _setup_window(self):
        self.setWindowTitle("Jensible (Verification Email)")
        self.setGeometry(250, 200, 1500, 1000)
        self.setStyleSheet(Styles['auth_window'])

    def _setup_layouts(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        central_widget.setLayout(self.main_layout)

        left_widget = QWidget()
        self.left_layout = QVBoxLayout(left_widget)

        right_widget = QWidget()
        self.right_layout = QVBoxLayout(right_widget)

        self.main_layout.addWidget(left_widget, 4)
        self.main_layout.addWidget(right_widget, 6)

    def _setup_phone_panel(self):
        phone_label = QLabel()
        phone_pixmap = QPixmap(IMAGE["phone"])
        phone_label.setPixmap(phone_pixmap)
        phone_label.setScaledContents(True)
        self.left_layout.addWidget(phone_label)

    def _setup_auth_login_panel(self):
        self._code_label()
        self._code_input()

    def _code_label(self):
        code_widget = QWidget()
        code_widget.setStyleSheet(Styles["speech_label"])
        code_layout = QHBoxLayout()
        code_widget.setLayout(code_layout)
        self.right_layout.addWidget(code_widget)

        code_label = QLabel("Верификация почты            ")
        code_label.setStyleSheet(Styles["login_label"])
        code_label.setMaximumWidth(1000)
        code_layout.addWidget(code_label)

        self.right_layout.setStretch(1, 1)

    def _code_input(self):
        code_input_widget = QWidget()
        code_input_widget.setStyleSheet(Styles["speech_label"])
        code_input_layout = QHBoxLayout()
        code_input_widget.setLayout(code_input_layout)
        self.right_layout.addWidget(code_input_widget)

        code_input = QLineEdit()
        code_input.setPlaceholderText("Введите код ...")
        code_input.setStyleSheet(Styles["login_input"])
        code_input.setMaximumWidth(1000)
        code_input_layout.addWidget(code_input)

        self.right_layout.setStretch(2, 0)