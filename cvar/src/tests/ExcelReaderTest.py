'''
Created on 2 Apr 2016

@author: Rolf
'''
import unittest
from lib.excel.data import Data
from lib.excel.excel_reader import ExcelReader
from root import Root
from datetime import datetime


class TestExcelReader(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = Data()
        self.data, wb = ExcelReader.read(self.data, Root.path() + '/../resources/test0.xlsm')
        wb.close()
        
    @classmethod
    def tearDownClass(self):
        self.data = None
       
    def test_lengthParameters(self):
        self.assertEquals(self.data.numberOfForwardProducts, 3, \
                          "Number of forward products doesn't match (preferred: 3, actual: " + str(self.data.numberOfForwardProducts) + ")")
        self.assertEquals(self.data.numberOfHpfcVectors, 4, \
                          "Number of HPFC vectors doesn't match (preferred: 4, actual: " + str(self.data.numberOfHpfcVectors) + ")")
        self.assertEquals(self.data.numberOfTimePeriods, 24, \
                          "Number of time intervals doesn't match (preferred: 24, actual: " + str(self.data.numberOfTimePeriods) + ")")
    
    def test_singleParameters(self):
        alpha = 0.8
        epsilon0 = 0.01
        self.assertEquals(self.data.alpha, alpha,
                          "Parameter 'alpha' doesn't match (preferred: " + str(alpha) + ", actual:" + str(self.data.alpha) + ")")
        self.assertEquals(self.data.eps0, 0.01,
                          "Parameter 'eps0' doesn't match (preferred: " + str(epsilon0) + ", actual:" + str(self.data.eps0) + ")")
        
    def test_1dArrayParameters(self):
        demand = [12, 8, 10, 7, 7, 13, 8, 18, 21, 23, 21, 17, 19, 19, 17, 20, 23, 17, 23, 14, 12, 8, 13, 7]
        forwardPrices = [900, 470, 430]
        for t in range(self.data.numberOfTimePeriods):
            self.assertEquals(self.data.demand[t+1], demand[t], \
                              "Demand[" + str(t+1) + "] doesn't match (preferred: " + str(demand[t]) + ", actual: " + str(self.data.demand[t+1]) + ")")
                          
        for f in range(self.data.numberOfForwardProducts):
            self.assertEquals(self.data.forwardPrices[f+1], forwardPrices[f], \
                              "Forward prices [" + str(f+1) + "] doesn't match" +  
                              "(preferred: " + str(forwardPrices[f]) + ", actual: " + str(self.data.forwardPrices[f+1]) + ")")
                          
    def test_forwardCharVectors(self):
        for t in range(self.data.numberOfTimePeriods):
            self.assertEquals(self.data.forwardCharVectors[(1,t+1)], 1, \
                              "Forward characteristic vector [1, " + str(t+1) + "] doesn't match" + 
                              "(preferred: 1, actual: " + str(self.data.forwardCharVectors[(1,t+1)]) + ")")
            if t < 8 or t >= 20:
                self.assertEquals(self.data.forwardCharVectors[(2,t+1)], 1, \
                              "Forward characteristic vector [2, " + str(t+1) + "] doesn't match" + 
                              "(preferred: 1, actual: " + str(self.data.forwardCharVectors[(2,t+1)]) + ")")    
                self.assertEquals(self.data.forwardCharVectors[(3,t+1)], 0, \
                              "Forward characteristic vector [3, " + str(t+1) + "] doesn't match" + 
                              "(preferred: 0, actual: " + str(self.data.forwardCharVectors[(3,t+1)]) + ")")    
            else:
                self.assertEquals(self.data.forwardCharVectors[(2,t+1)], 0, \
                              "Forward characteristic vector [2, " + str(t+1) + "] doesn't match" + 
                              "(preferred: 0, actual: " + str(self.data.forwardCharVectors[(2,t+1)]) + ")")    
                self.assertEquals(self.data.forwardCharVectors[(3,t+1)], 1, \
                              "Forward characteristic vector [3, " + str(t+1) + "] doesn't match" + 
                              "(preferred: 1, actual: " + str(self.data.forwardCharVectors[(3,t+1)]) + ")")                        
    
    def test_hpfcVectors(self):
        hpfcVector = [[47.83, 44.83, 42.23, 38.97, 36.72, 38.26, 31.53, 31.02, 39.41, 43.73, 46.06, 49.94, 50.84, 45.11, 43.07, 41.70, 41.22, 47.87, 60.92, 63.93, 61.07, 54.90, 60.03, 52.81], \
                      [48.46, 39.18, 40.81, 28.55, 26.84, 38.34, 30.67, 29.31, 38.22, 31.81, 43.85, 45.20, 48.96, 43.42, 40.45, 43.34, 45.96, 48.06, 52.79, 73.36, 61.52, 54.77, 47.56, 58.18], \
                      [47.43, 32.61, 37.54, 36.11, 27.36, 39.31, 30.20, 25.45, 47.20, 37.18, 59.80, 44.01, 45.81, 46.01, 37.87, 46.80, 48.58, 54.67, 60.11, 71.95, 72.62, 49.59, 50.99, 47.87], \
                      [39.98, 30.43, 36.63, 31.73, 28.95, 36.04, 33.50, 28.02, 50.24, 29.94, 55.96, 47.54, 45.49, 49.56, 38.51, 48.44, 47.10, 53.12, 58.17, 76.06, 72.08, 42.23, 49.61, 54.65]]
        for t in range(self.data.numberOfTimePeriods):
            for s in range(self.data.numberOfHpfcVectors):
                self.assertEquals(self.data.hpfcVectors[(s+1, t+1)], hpfcVector[s][t], \
                                  "HPFC vector [" + str(s) + ", " + str(t) + "] doesn't match" +
                                  "(preferred: " + str(hpfcVector[s][t]) + ", actual: " + str(self.data.hpfcVectors[(s+1,t+1)]) + ")")
    
    def test_labels(self):
        forwardProductNames = ["BL", "PL", "OL"]
        for i in range(24):
            self.assertEquals(self.data.timePeriodNames[i],
                              datetime(2011, 4, 1, i, 0),
                              "Incorrect data for the name of " + str(i+1) + ". hedging period: " + 
                              "\npreferred: " + str(datetime(2011, 4, 1, i, 0)) + 
                              "\nactual:    " + str(self.data.timePeriodNames[i]))
        self.assertEquals(self.data.forwardNames,
                          forwardProductNames,
                              "Incorrect data for the forward product names: " + 
                              "\npreferred: " + str(forwardProductNames) + 
                              "\nactual:    " + str(self.data.forwardNames))                   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    