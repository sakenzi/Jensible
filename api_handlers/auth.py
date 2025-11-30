from dotenv import load_dotenv
import requests
import os


load_dotenv()

api = os.getenv("API_BASE_URL")

def register(data):
    url = f"{api}/auth/register"
    print("Отправка на регистрацию:", data)
    try:
        response = requests.post(url, json=data, timeout=10)
        print(f"Ответ сервера: {response.status_code} {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка регистрации {e}")
        return None

def verification_email(data):
    url = f"{api}/auth/verification"
    print("Отправка кода:", data)
    try:
        response = requests.post(url, json=data, timeout=10)
        print(f"Ответ верификации: {response.status_code} {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка верификаций почты {e}")
        return None
        
def login(data):
    url = f"{api}/auth/login"
    print("Логин:", data)
    try:
        response = requests.post(url, json=data, timeout=10)
        print(f"Ответ логина: {response.status_code} {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка логина {e}")
        return None