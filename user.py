from credentials import Credentials
'''
import Credentials class from credentials module
'''

class User:
    '''
    user class that generates instances of a user's account
    '''

    user_list = []

    def __init__(self, user_name, user_password):
        '''
        __init__ method to define the properties of a User object

        Args:
            user_name: user's name
            user_password: user's password
        '''
        
        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        '''
        Method that saves a user to the user list
        '''

        User.user_list.append(self)

    @classmethod
    def find_credential(cls, name):
        '''
        Method that checks if Credentials class is imported

        Args: 
            name: name of credential

        Returns:
               Boolean: True/False whether credential exists or not
        '''

        for credential in Credentials.Credentials_list:
            if credential.credential_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):
        '''
        method that allows users to logi to their password locker account

        Args:
            name: name of user
            password: password of user

        Returns:
               credentials list of user according to name and password
               False: if name or password is incorrect
        '''

        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credentials.Credentials_list

        return False

    @classmethod
    def display_user(cls):
        '''
        method that displays user list
        '''

        return cls.user_list

    @classmethod
    def user_exists(cls, name):
        '''
        method that checks if user exists in user list

        Args:
            name: name of user to search

        Returns:
               Boolean:True/False whether the user exists or not
        '''

        for user in cls.user_list:
            if user.user_name == name:
                return True

        return False