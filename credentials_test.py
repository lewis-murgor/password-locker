
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

        self.new_credential = Credentials("murgor", "Instagram", "POg6oom!")

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
        self.assertEqual( self.new_credential.credential_name, "Instagram" )
        self.assertEqual( self.new_credential.credential_password, "POg6oom!" )

    def test_store_credential(self):
        '''
        test_store_credential test case to test if the credential object is saved into the credentials list
        '''

        self.new_credential.store_credential()
        self.assertEqual(len(Credentials.Credentials_list),1)

    def test_store_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential objects to our contact_list
        '''

        self.new_credential.store_credential()
        test_credential = Credentials("kiplagat", "Twitter", "Twitterx29")
        test_credential.store_credential()

        self.assertEqual(len(Credentials.Credentials_list),2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential account from our credentials list
        '''

        self.new_credential.store_credential()
        test_credential = Credentials("kiplagat", "Twitter", "Twitterx29")
        test_credential.store_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.Credentials_list),1)

    def test_generate_password(self):
        '''
        test_generate_password to test if we can generate a password for credential accounts
        '''

        generated_password = self.new_credential.generate_password()

        self.assertEqual( len(generated_password), 8 )



if __name__ == '__main__':
    unittest.main()