
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