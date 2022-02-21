#!/usr/bin/env python3.8


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

def save_users(User):
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

def create_credential(user_password, name, password):
    '''
    Function to create a credential

    Args:
        user_password: password used to create user account
        name: name of credential account
        password: password for credential account
    '''

    new_credential = Credentials(user_password, name, password)

    return new_credential

def save_credentials(Credentials):
    '''
    Function that saves a credential

    Args:
        credential: credential to be saved
    '''

    Credentials.store_credential()

def delete_credential(credential):
    '''
    Function that deletes a credential

    Args:
        credential: credential to be deleted
    '''

    Credentials.delete_credential()

def check_existing_credentials(name):
    '''
    Function that checks if a user credential name already exists

    Args:
        name: name of credential to search
    '''

    return Credentials.credential_exists(name)

def display_credentials(password):
    '''
    Function that returns saved credentials

    Args:
        password: password for user account
    '''

    return Credentials.display_credentials(password)

def create_generated_password(name):
    '''
    Function that generates a password for the user

    Args:
        name: name of credential account
    '''

    password = Credentials.generate_password()

    return password

def main():
    '''
    Function running the password-locker
    '''

    print('''Welcome to password-locker \n
    Use this short codes to get arround ''')

    while True:
        '''
        Loop running the entire application
        '''

        print(''' Short codes:
        cu - create a password-locker account \n
        du - display names of current password-locker users \n
        lg - log into your password-locker account \n
        ex - exit the password-locker account''')

        short_code = input().lower()

        if short_code == 'cu':
            '''
            Creating a password-locker account
            '''

            print("\n")
            print("New Password Locker Account")
            print("-"*10)

            print("username...")
            user_name = input()

            print("Password ...")
            user_password = input()

            save_users(create_user(user_name, user_password))

            print("\n")
            print(f"Welcome to Password Locker {user_name}")
            print("\n")

        elif short_code == 'du':
            '''
            Display names of all users
            '''

            if display_users():
                print("\n")
                print("Here are the current users of Password Locker")
                print("-"*10)

                for user in display_users():
                    print(f"{user.user_name}")
                    print("-"*10)
            else:
                print("\n")
                print("Password Locker has no current user.\n    Be the first user :)")
                print("\n")

        elif short_code == 'lg':
            '''
            Logs in the user to their Password Locker account
            '''

            print("\n")
            print("Log into Password Locker Account")
            print("Enter your user name")
            user_name = input()

            print("Enter your password")
            user_password = input()

            if user_log_in(user_name,user_password) == None:

                print("\n")
                print("Please try again or create an account")
                print("\n")

            else:

                user_log_in(user_name,user_password)
                print("\n")
                print(f'''Welcome to your Credentials {user_name} \n
                Use these short codes to get around''')

                while True:
                    '''
                    Loop to run credential functions
                    '''

                    print('''  Short codes:
        cc - add a credential \n
        dlc - delete credentials \n
        dc - display credentials \n
        cg - create a credential with a generate password \n
        ex - exit Credentials''')
                    
                    short_code = input().lower()

                    if short_code == 'cc':
                        '''
                        Creating a credential
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        print("Password of the credential ...")
                        credential_password = input()

                        save_credentials(create_credential(user_password, credential_name, credential_password))

                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                    elif short_code == 'dlc':
                        '''
                        Deleting a credential
                        '''

                        print("\n")
                        print("Delete credential")
                        print("-"*10)

                        print("Name of credential...")
                        credential_name = input()

                        print("Password of the credential ...")
                        credential_password = input()

                        delete_credential(create_credential(user_password, credential_name, credential_password))

                        print("\n")
                        print(f"Credentials for {credential_name} have been deleted")
                        print("\n")

                    elif short_code == 'dc':
                        '''
                        Displaying credential name and password
                        '''

                        if display_credentials(user_password):
                            print("\n")
                            print(f"{user_name}\'s credentials")
                            print("-"*10)

                            for credential in display_credentials(user_password):
                                print(f"Account ..... {credential.credential_name}")
                                print(f"Password .... {credential.credential_password}")
                                print("-"*10)

                        else:
                            print("\n")
                            print("You have no credentials")
                            print("\n")

                    elif short_code == 'cg':
                        '''
                        Creating a credential with a generated password
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        save_credentials(Credentials(user_password, credential_name, (create_generated_password(credential_name))))

                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                    elif short_code == 'ex':
                        print(f"Byee {user_name}")
                        print("\n")
                        break

                    else:
                        print("\n")
                        print(f'''{short_code} does not compute.
    Please use the short codes''')
                        print("\n")

        elif short_code == 'ex':
            '''
            Exit Password Locker.
            '''
            print("\n")
            print("Bye ...")

            break

        else:
            print("\n")
            print(f'''Come again, what's {short_code}?
    Please use the short codes''')
            print("\n")





if __name__ == '__main__':
    main()
