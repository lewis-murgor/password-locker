
import unittest
from credentials import Credentials
'''
import unittest to create tests for credentials
import Credentials class to be tested
'''

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        self.new_credential = Credentials("murgor", "instagram", "POg6oom!")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Credentials.Credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual( self.new_credential.user_password, "murgor")
        self.assertEqual( self.new_credential.credential_name, "instagram" )
        self.assertEqual( self.new_credential.credential_password, "POg6oom!" )

if __name__ == '__main__':
    unittest.main()