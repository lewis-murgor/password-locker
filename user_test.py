

import unittest
from user import User
from credentials import Credentials
'''
import unittest to create tests for User module
import User class to be tested
'''

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        self.new_user = User("Lewis", "schinchilla")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual( self.new_user.user_name, "Lewis" )
        self.assertEqual( self.new_user.user_password, "schinchilla" )

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''

        self.new_user.save_user()

        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user objects to our user_list
        '''

        self.new_user.save_user()
        test_user = User("Fabian", "king")
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_find_credential(self):
        '''
        test_find_credential to check if credentials module is being imported correctly
        '''

        self.new_user.save_user()
        test_user = User("Fabian", "king")
        test_user.save_user()

        found_credential = User.find_credential("Fabian")
        self.assertEqual( found_credential, False )

    def test_log_in(self):
        '''
        test_log_in to test if users can login to their password-locker account
        '''

        self.new_user.save_user()
        test_user = User("Fabian", "king")
        test_user.save_user()

        account = User.log_in("Fabian", "king")
        self.assertEqual(account, Credentials.Credentials_list)

    def test_display_user(self):
        '''
        test_display_user to test if a user can view list of users
        '''

        self.assertEqual(User.display_user() , User.user_list)

    def test_user_exists(self):
        '''
        test_user_exists to test if we can search for a user
        '''

        self.new_user.save_user()
        test_user = User("Fabian", "king")
        test_user.save_user()

        user_exists = User.user_exists("Fabian")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()