import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
)
from views.auth_window.auth_register import AuthRegisterWindow
from views.auth_window.auth_login import AuthLoginWindow
from views.auth_window.auth_verification import AuthVerificationEmail


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class ApplicationManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = AuthLoginWindow(self)
        self.register_window = None
        self.verification_window = None
        self.main_window = None
        self.token = None
        self.websocket = None
        self.controller = None

    def show_login_window(self):
        self.login_window.show()
        if self.register_window:
            self.register_window.hide()

    def show_register_window(self):
        if not self.register_window:
            self.register_window = AuthRegisterWindow(self)
        self.register_window.show()
        self.login_window.hide()

    def show_verification_window(self, email=None):
        if not self.verification_window:
            self.verification_window = AuthVerificationEmail(self)
        self.verification_window.set_email(email)
        self.verification_window.show()
        if self.register_window:
            self.register_window.hide()

    def run(self):
        self.show_login_window()
        sys.exit(self.app.exec_())