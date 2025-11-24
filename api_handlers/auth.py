from dotenv import load_dotenv
import requests
import os


load_dotenv()

api = os.getenv("API_BASE_URL")

def register(data):
    url = f"{api}/v1/auth/register"
    print(data)
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка регистрации {e}")

def verification_email(data):
    url = f"{api}/v1/auth/verification"
    print(data)
    try:
        response = requests.post(url, json=data)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка верификаций почты {e}")
        
def login(data):
    url = f"{api}/v1/auth/login"
    print(data)
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка логина {e}")