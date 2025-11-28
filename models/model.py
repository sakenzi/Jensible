class AuthRegisterData:
    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password
        }
    

class AuthVerificationEmailData:
    def __init__(self, email, code):
        self.email = email
        self.code = code

    def to_dict(self):
        return {
            "email": self.email,
            "code": self.code
        }
    

class AuthLoginData:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password
        }