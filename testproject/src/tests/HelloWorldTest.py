'''
Created on 25 Apr 2016

@author: Rolf
'''
import unittest
from lib.stuff import HelloWorldClass


class TestHelloWorld(unittest.TestCase):


    def testHelloWorld(self):
        message = HelloWorldClass.helloWorld()
        self.assertEquals(message, "Hello World!", "The message is '" + message + "', and not 'Hello World!'.")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()