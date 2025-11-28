from models.model import (
    AuthRegisterData,
    AuthVerificationEmailData,
    AuthLoginData,
)
from api_handlers.auth import (
    register as register_request,
    verification_email as verification_email_request,
    login as login_request,
)


class AuthWindowController:
    def __init__(self, window=None):
        self.window = window
        self.token=None

    def handle_login(self, email, password):
        if not email or not password:
            print("Поля не должно быть пустым")
            return False, "Поля не должно быть пустым"
        
        data = AuthLoginData(email, password).to_dict()
        response = login_request(data)

        if response:
            json_response = response.json()
            if "access_token" in json_response:
                self.token = json_response["access_token"]
                print(f"Токен: {self.token}")

        if response is not None:
            if response.status_code == 200:
                print("Успешный вход")
                print(response.json())
                return True, "Успешный вход"
            else:
                print("Ошибка входа")
                return False, f"Ошибка входа: {response.status_code}"
            
        else:
            return False, "Ошибка сети или сервера"
        
    def handle_register(self, full_name, email, password):
        if not full_name or not email or not password:
            return False, "Все поля должны быть заполнены"

        data = AuthRegisterData(full_name, email, password).to_dict()
        response = register_request(data)

        if response is None:
            return False, "Ошибка сети или сервера"

        try:
            json_response = response.json()
        except ValueError:
            return False, "Некорректный ответ от сервера"

        status_code = json_response.get("status_code")
        message = json_response.get("message", "Неизвестная ошибка")

        if status_code == 0:
            print("Успешная регистрация (письмо отправлено)")
            print(f"Сообщение от сервера: {message}")
            return True, message
        else:
            print(f"Ошибка регистрации: {message}")
            return False, message
        
    def handle_verification_email(self, email, code):
        if not email or not code:
            print("Поля не должно быть пустым")
            return False, "Поля не должны быть пустыми"
        
        data = AuthVerificationEmailData(email, code).to_dict()
        response = verification_email_request(data)

        if response:
            json_response = response.json()
            if "access_token" in json_response:
                self.token = json_response["access_token"]
                print(f"Токен: {self.token}")

        if response is not None:
            if response.status_code == 200:
                print("Успешная верификация почты")
                print(response.json())
                return True, "успешная верификация"
            else:
                print("Ошибка верификаций")
                return False, f"Ошибка верификаций: {response.status_code}"
        else:
            return False, "Ошибка сети или сервера"
        
    def get_token(self):
        return self.token