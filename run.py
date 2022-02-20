

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

def save_users(user):
    '''
    Function that saves a user account

    Args:
        user: user account to be saved
    '''

    User.save_user()

def check_existing_users(name):
    '''
    Function that checks if a username already exists

    Args:
        name: user account name
    '''

    return User.user_exists(name)

def user_log_in(name, password):
    '''
    Function that allows users to login to their account

    Args:
        name: name used to create user account
        password: password used to create user account
    '''

    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)

def display_users():
    '''
    Function that returns all saved users
    '''

    return User.display_user()
