'''
Created on 31 Mar 2016

@author: Rolf
'''
import reprlib # kell hozza a 'future' package: 'conda install future'

class Data(object):


    def __init__(self):
        self.numberOfTimePeriods = 0
        self.numberOfForwardProducts = 0
        self.numberOfHpfcVectors = 0
        self.alpha = 0
        self.eps0 = 0
                
        self.demand = {}
        self.forwardCharVectors = {}
        self.forwardPrices = {}
        self.hpfcVectors = {}
        
        self.timePeriodNames = []
        self.forwardNames = []
        self.demandAsArray = []
    
        self.name = ""
        
        self.dictionary = {}
    
    def initialise(self):
        self.dictionary = { None: 
                            {'t' : {None : self.numberOfTimePeriods},
                             'f' : {None : self.numberOfForwardProducts},
                             's' : {None : self.numberOfHpfcVectors},
                             'D_params' : self.demand,
                             'A_params' : self.forwardCharVectors,
                             'P0_params' : self.forwardPrices,
                             'eps0_param' : {None : self.eps0},
                             'y_params' : self.hpfcVectors,
                             'alpha_param' : {None : self.alpha}
                             }
                           }
        
    def items(self):
        return {attr:getattr(self, attr) for attr in vars(self)}
    
    @staticmethod
    def _pprint(r, k, v):
        return r.repr(k) + ": " + r.repr(v) 
        
    def pprint(self, maxlength=None, filepath=None):
        r = reprlib.Repr()
        r.maxother = 40 # for datetime.datetime() objects
        if maxlength:
            r.maxlist = maxlength
            r.maxset = maxlength
            r.maxarray = maxlength
            r.maxdict = maxlength
        if filepath:
            f = open(filepath, 'w')
            for k, v in self.items().iteritems():
                print >> f, self._pprint(r, k, v)
            f.close()
        else:
            for k, v in self.items().iteritems():
                print self._pprint(r, k, v)
            