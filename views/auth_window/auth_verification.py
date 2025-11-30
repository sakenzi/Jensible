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
from controllers.auth_controller import AuthWindowController


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class AuthVerificationEmail(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        self.email = None
        self._setup_window()
        self._setup_layouts()
        self._setup_phone_panel()
        self._setup_auth_login_panel()
        self.controller = AuthWindowController()

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
        self._email_label()
        self._email_input()
        self._code_label()
        self._code_input()

    def _email_label(self):
        email_widget = QWidget()
        email_widget.setStyleSheet(Styles["speech_label"])
        email_layout = QHBoxLayout()
        email_widget.setLayout(email_layout)
        self.right_layout.addWidget(email_widget)

        self.email_label = QLabel("Введите почту повторно")
        self.email_label.setStyleSheet(Styles["login_label"])
        self.email_label.setMaximumWidth(1000)
        email_layout.addWidget(self.email_label)

        self.right_layout.setStretch(4, 0)

    def _email_input(self):
        email_input_widget = QWidget()
        email_input_widget.setStyleSheet(Styles["speech_label"])
        email_input_layout = QHBoxLayout()
        email_input_widget.setLayout(email_input_layout)
        self.right_layout.addWidget(email_input_widget)

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

    def _sign_up(self):
        sign_up_widget = QWidget()
        sign_up_widget.setStyleSheet(Styles['emblem_widget'])
        sign_up_layout = QHBoxLayout()
        sign_up_widget.setLayout(sign_up_layout)
        self.right_layout.addWidget(sign_up_widget)

        sign_up_button = QPushButton("Sign Up")
        sign_up_button.setStyleSheet(Styles['sign_in_button'])
        sign_up_layout.addWidget(sign_up_button)

        self.right_layout.setStretch(8, 1)
    
        sign_up_button.clicked.connect(self.on_verification_button_clicked)

    def set_email(self, email):
        self.email = email
        self.email_label.setText(f"Код отправлен на: {email}")  
        print(f"Окно верификации: код нужно ввести для {email}")

    def on_verification_button_clicked(self):
        success, message = self.controller.handle_verification_email(
            self.username_input.text(),
            self.fullname_input.text(),
            self.password_input.text()
        )
        if success:
            token = self.controller.get_token()
            self.app_manager.set_token(token)
            self.app_manager.show_main_window()
            self.hide()