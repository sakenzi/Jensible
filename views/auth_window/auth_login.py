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
    QSpacerItem,
)
from PyQt5.QtCore import (
    QPersistentModelIndex,
    Qt,
)
from PyQt5.QtGui import (
    QPixmap,
)
import sys
import os
from resources.styles.auth_login_components import Styles
from resources.icons.auth_login_icons import ICONS
from resources.images.auth_login_images.auth_login_images import IMAGE


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class AuthLoginWindow(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        self._setup_window()
        self._setup_layouts()
        self._setup_phone_panel()
        self._setup_auth_login_panel()

    def _setup_window(self):
        self.setWindowTitle("Jensible (Login)")
        self.setGeometry(250, 200, 1500, 1000)
        self.setStyleSheet(Styles["auth_window"])

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
        self._welcome_speech()
        self._login_label()
        self._login_input()
        self._password_label()
        self._password_input()
        self._sign_in()

    def _welcome_speech(self):
        speech_widget = QWidget()
        speech_widget.setStyleSheet(Styles["speech_label"])
        speech_layout = QHBoxLayout()
        speech_widget.setLayout(speech_layout)
        self.right_layout.addWidget(speech_widget)

        speech_label = QLabel("Войдите в систему Jensible                ")
        speech_label.setStyleSheet(Styles["speech_label"])
        speech_label.setMaximumWidth(1000)
        speech_layout.addWidget(speech_label)
    
        self.right_layout.setStretch(1, 1)

    def _login_label(self):
        login_widget = QWidget()
        login_widget.setStyleSheet(Styles["speech_label"])
        login_layout = QHBoxLayout()
        login_widget.setLayout(login_layout)
        self.right_layout.addWidget(login_widget)

        login_label = QLabel("Почта")
        login_label.setStyleSheet(Styles["login_label"])
        login_label.setMaximumWidth(1000)
        login_layout.addWidget(login_label)

        self.right_layout.setStretch(2, 1)

    def _login_input(self):
        login_input_widget = QWidget()
        login_input_widget.setStyleSheet(Styles["speech_label"])
        login_input_layout = QHBoxLayout()
        login_input_widget.setLayout(login_input_layout)
        self.right_layout.addWidget(login_input_widget)

        login_input = QLineEdit()
        login_input.setPlaceholderText("Введите почту ...")
        login_input.setStyleSheet(Styles["login_input"])
        login_input.setMaximumWidth(1000)
        login_input_layout.addWidget(login_input)

        self.right_layout.setStretch(3, 1)

    def _password_label(self):
        password_widget = QWidget()
        password_widget.setStyleSheet(Styles["speech_label"])
        password_layout = QHBoxLayout()
        password_widget.setLayout(password_layout)
        self.right_layout.addWidget(password_widget)

        login_label = QLabel("Пароль")
        login_label.setStyleSheet(Styles["login_label"])
        login_label.setMaximumWidth(1000)
        password_layout.addWidget(login_label)

        self.right_layout.setStretch(4, 1)

    def _password_input(self):
        password_input_widget = QWidget()
        password_input_widget.setStyleSheet(Styles["speech_label"])
        password_input_layout = QHBoxLayout()
        password_input_widget.setLayout(password_input_layout)
        self.right_layout.addWidget(password_input_widget)

        password_input = QLineEdit()
        password_input.setPlaceholderText("Введите пароль ...")
        password_input.setStyleSheet(Styles["login_input"])
        password_input.setMaximumWidth(1000)
        password_input_layout.addWidget(password_input)

        self.right_layout.setStretch(5, 1)

    def _sign_in(self):
        sign_in_widget = QWidget()
        sign_in_widget.setStyleSheet(Styles["speech_label"])
        sign_in_layout = QHBoxLayout()
        sign_in_widget.setLayout(sign_in_layout)
        self.right_layout.addWidget(sign_in_widget)

        sign_in_button = QPushButton("Войти")
        sign_in_button.setStyleSheet(Styles["sign_in_button"])
        sign_in_button.setMaximumWidth(1000)
        sign_in_layout.addWidget(sign_in_button)

        self.right_layout.setStretch(6, 1)

    