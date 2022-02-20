from credentials import Credentials

class User:

    user_list = []

    def __init__(self, user_name, user_password):
        
        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):

        User.user_list.append(self)

    @classmethod
    def find_credential(cls, name):

        for credential in Credentials.Credentials_list:
            if credential.credential_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):

        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credentials.Credentials_list

        return False

    @classmethod
    def display_user(cls):

        return cls.user_list

    @classmethod
    def user_exists(cls, name):

        for user in cls.user_list:
            if user.user_name == name:
                return True

        return False