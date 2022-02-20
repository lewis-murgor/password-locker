

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

if __name__ == '__main__':
    unittest.main()