from random import choice
import string
'''
Import random and string modules from Python for generating passwords
'''

class Credentials:
    '''
    Class that generates new instances of user's credentials
    '''

    Credentials_list = []

    def __init__(self, user_password, credential_name, credential_password):
        '''
        __init__ method that defines properties for a user object.

        Args:
            user_password: users password
            credential_name: name of account
            credential_password: password of account
        '''

        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

    def store_credential(self):
        '''
        method that saves user's credentials to the credentials list.
        '''

        Credentials.Credentials_list.append(self)

    def delete_credential(self):
        '''
        method that deletes user's credentials from the credentials list.
        '''

        Credentials.Credentials_list.remove(self)

    @classmethod
    def generate_password(cls):

        '''
        Method that generates a random password.
        '''

        size = 8

        new_password = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

        password = "".join(choice(new_password) for number in range (size))

        return password

    @classmethod
    def display_credentials(cls, password):
        '''
        method that displays the credentials list.
        '''

        user_Credentials_list = []

        for credential in cls.Credentials_list:
            if credential.user_password == password:
                user_Credentials_list.append(credential)

        return user_Credentials_list

    @classmethod
    def credential_exists(cls, name):
        '''
        method that checks if a credential exists in the credentials list
        '''

        for credential in cls.Credentials_list:
            if credential.credential_name == name:
                return True

        return False
