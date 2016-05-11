'''
Created on 31 Mar 2016

@author: Rolf
'''

class Data(object):


    def __init__(self):
        self.numberOfTimeIntervals = 0
        self.numberOfForwardProducts = 0
        self.numberOfHpfcVectors = 0
        self.alpha = 0
        self.epsilon0 = 0
        self.T = 0
                
        self.demand = {}
        self.forwardCharVectors = {}
        self.forwardPrices = {}
        self.hpfcVectors = {}
        
        self.hedgingPeriodNames = []
        self.forwardProductNames = []
        self.demandAsArray = []
    