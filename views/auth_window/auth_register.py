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

class AuthRegisterWindow(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        self._setup_window()

    def _setup_window(self):
        self.setWindowTitle("Jensible (Register)")
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
        self._welcome_speech()
        self._fullname_label()
        self._fullname_input()
        self._email_label()
        self._email_input()
        self._password_label()
        self._email_input()
        
    def _welcome_speech(self):
        speech_widget = QWidget()
        speech_widget.setStyleSheet(Styles["speech_label"])
        speech_layout = QHBoxLayout()
        speech_widget.setLayout(speech_layout)
        self.right_layout.addWidget(speech_widget)

        speech_label = QLabel("Зарегистрируйтесь в системе Jensible            ")
        speech_label.setStyleSheet(Styles["speech_label"])
        speech_label.setMaximumWidth(1000)
        speech_layout.addWidget(speech_label)

        self.right_layout.setStretch(1, 1)

    def _fullname_label(self):
        fullname_widget = QWidget()
        fullname_widget.setStyleSheet(Styles["speech_label"])
        fullname_layout = QHBoxLayout()
        fullname_widget.setLayout(fullname_layout)
        self.right_layout.addWidget(fullname_widget)

        fullname_label = QLabel("Имя пользователя")
        fullname_label.setStyleSheet(Styles["login_label"])
        fullname_label.setMaximumWidth(1000)
        fullname_layout.addWidget(fullname_label)

        self.right_layout.setStretch(2, 0)

    def _fullname_input(self):
        fullname_input_widget = QWidget()
        fullname_input_widget.setStyleSheet(Styles["speech_label"])
        fullname_input_layout = QHBoxLayout()
        fullname_input_widget.setLayout(fullname_input_layout)
        self.right_layout.addWidget(fullname_input_widget)

        fullname_input = QLineEdit()
        fullname_input.setPlaceholderText("Введите имю пользователя ...")
        fullname_input.setStyleSheet(Styles["login_input"])
        fullname_input.setMaximumWidth(1000)
        fullname_input_layout.addWidget(fullname_input)

        self.right_layout.setStretch(3, 0)

    def _email_label(self):
        email_widget = QWidget()
        email_widget.setStyleSheet(Styles["speech_label"])
        email_layout = QHBoxLayout()
        email_widget.setLayout(email_layout)
        self.right_layout.addWidget(email_widget)

        email_label = QLabel("Почта")
        email_label.setStyleSheet(Styles["login_label"])
        email_label.setMaximumWidth(1000)
        email_layout.addWidget(email_label)

        self.right_layout.setStretch(4, 0)

    def _email_input(self):
        email_input_widget = QWidget()
        email_input_widget.setStyleSheet(Styles["speech_label"])
        email_input_layout = QHBoxLayout()
        email_input_widget.setLayout(email_input_layout)
        self.right_layout.addWidget(email_input_widget)

        email_input = QLineEdit()
        email_input.setPlaceholderText("Введите почту ...")
        email_input.setStyleSheet(Styles["login_input"])
        email_input.setMaximumWidth(1000)
        email_input_layout.addWidget(email_input)

        self.right_layout.setStretch(5, 0)

    def _password_label(self):
        password_widget = QWidget()
        password_widget.setStyleSheet(Styles["speech_label"])
        password_layout = QHBoxLayout()
        password_widget.setLayout(password_layout)
        self.right_layout.addWidget(password_widget)

        password_label = QLabel("Пароль")
        password_label.setStyleSheet(Styles["login_label"])
        password_label.setMaximumWidth(1000)
        password_layout.addWidget(password_label)

        self.right_layout.setStretch(6, 0)

    def _password_input(self):
        password_input_widget = QWidget()
        password_input_widget.setStyleSheet(Styles["speech_label"])
        password_input_layout = QHBoxLayout()
        password_input_widget.setLayout(password_input_layout)
        self.right_layout.addWidget(password_input_widget)

        password_input = QLineEdit()
        password_input.setPlaceholderText("Придумайте пароль ...")
        password_input.setStyleSheet(Styles["login_input"])
        password_input.setMaximumWidth(1000)
        password_input_layout.addWidget(password_input)

        self.right_layout.setStretch(7, 0)