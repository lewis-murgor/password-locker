

from user import User
from credentials import Credentials
'''
import user class from user module
import credentials class from credentials module
'''

def create_user(name, password):
    '''
    Function to create a user password - locker account

    Args:
        name: the name the user wants for the account
        password: password user wants for the account
    '''

    new_user = User(name, password)

    return new_user
