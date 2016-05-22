'''
Created on 2 Apr 2016

@author: Rolf
'''
import unittest
from tools import Tools


class TestTools(unittest.TestCase):

    def test_ListToDict1D(self):
        testArray = [2, 3.333, 5, 7, 11.5]
        testDict = {1:2, 2:3.333, 3:5, 4:7, 5:11.5}
        self.assertEqual(Tools.ListToDict1D(testArray), testDict, \
                         "ListToDict1D not working properly:\n" + 
                         "preferred: " + str(testDict) +
                         "\n   actual: " + str(Tools.ListToDict1D(testArray)) ) 
        
    def test_ListToDict2D(self):
        testArray = [[2, 3.5, 5, 7.5, 11], [1.1, 4, 9.9, 16, 25.25]]
        testDict = {(1,1):2, (1,2):3.5, (1,3):5, (1,4):7.5, (1,5):11, \
                    (2,1):1.1, (2,2):4, (2,3):9.9, (2,4):16, (2,5):25.25}
        self.assertEqual(Tools.ListToDict2D(testArray), testDict, \
                         "ListToDict2D not working properly:\n" + 
                         "preferred: " + str(testDict) +
                         "\n   actual: " + str(Tools.ListToDict2D(testArray)) ) 
    
    def test_Transpose(self):
        testArray = [[2, 3.5, 5, 7.5, 11], [1.1, 4, 9.9, 16, 25.25]]
        transposedArray = [[2, 1.1], [3.5, 4], [5, 9.9], [7.5, 16], [11, 25.25]]
        self.assertEqual(Tools.Transpose(testArray), transposedArray, \
                         "Transpose not working properly:\n" + 
                         "preferred: " + str(transposedArray) +
                         "\n   actual: " + str(Tools.Transpose(testArray)) ) 

    def test_Logger(self):
        print "TODO Logger Test"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()