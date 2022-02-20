from random import choice
import string

class Credentials:

    Credentials_list = []

    def __init__(self, user_password, credential_name, credential_password):

        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

    def store_credential(self):

        Credentials.Credentials_list.append(self)

    def delete_credential(self):

        Credentials.Credentials_list.remove(self)

    @classmethod
    def generate_password(cls):

        '''
        Method that generates a random alphanumeric password
        '''

        size = 7

        new_password = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

        password = "".join(choice(new_password) for number in range (size))

        return password

    @classmethod
    def display_credentials(cls, password):

        user_Credentials_list = []

        for credential in cls.Credentials_list:
            if credential.user_password == password:
                user_Credentials_list.append(credential)

        return user_Credentials_list
