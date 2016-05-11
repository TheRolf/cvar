'''
Created on 3 Apr 2016

@author: Rolf
'''

import unittest

from pyomo.core.base.numvalue import value
from pyomo.core.base.set_types import Reals, NonNegativeReals

from lib.excel.data import Data
from lib.pyomo.initialiser import Initialiser
from tools import Tools

class TestPyomoModel(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = Data()
        self.data.numberOfForwardProducts = 3
        self.data.numberOfHpfcVectors = 4
        self.data.numberOfTimeIntervals = 24
        
        self.data.alpha = 0.8
        self.data.epsilon0 = 0.01
        self.data.T = 0
        
        self.data.demand = Tools.ListToDict1D([12, 8, 10, 7, 7, 13, 8, 18, 21, 23, 21, 17, 19, 19, 17, 20, 23, 17, 23, 14, 12, 8, 13, 7])
        self.data.forwardCharVectors = Tools.ListToDict2D([[1 for i in range(24)],  # @UnusedVariable
                                                      [1 if (i<8 or i>=20) else 0 for i in range(24)],
                                                      [0 if (i<8 or i>=20) else 1 for i in range(24)]
                                                      ])
        self.data.forwardPrices = Tools.ListToDict1D([24, 20, 20])
        self.data.hpfcVectors = Tools.ListToDict2D([[47.83, 44.83, 42.23, 38.97, 36.72, 38.26, 31.53, 31.02, 39.41, 43.73, 46.06, 49.94, 50.84, 45.11, 43.07, 41.70, 41.22, 47.87, 60.92, 63.93, 61.07, 54.90, 60.03, 52.81], \
                            [48.46, 39.18, 40.81, 28.55, 26.84, 38.34, 30.67, 29.31, 38.22, 31.81, 43.85, 45.20, 48.96, 43.42, 40.45, 43.34, 45.96, 48.06, 52.79, 73.36, 61.52, 54.77, 47.56, 58.18], \
                            [47.43, 32.61, 37.54, 36.11, 27.36, 39.31, 30.20, 25.45, 47.20, 37.18, 59.80, 44.01, 45.81, 46.01, 37.87, 46.80, 48.58, 54.67, 60.11, 71.95, 72.62, 49.59, 50.99, 47.87], \
                            [39.98, 30.43, 36.63, 31.73, 28.95, 36.04, 33.50, 28.02, 50.24, 29.94, 55.96, 47.54, 45.49, 49.56, 38.51, 48.44, 47.10, 53.12, 58.17, 76.06, 72.08, 42.23, 49.61, 54.65]])

        self.model = Initialiser.init(self.data)
        
    @classmethod
    def tearDownClass(self):
        self.model = None

    def test_variables(self):

        self.assertEquals( self.model.x_vars.domain, Reals, \
                           "Incorrect domain for 'x', expected: 'Reals', actual: '" + str(self.model.x_vars.domain) + "'")
        self.assertEquals( self.model.x_vars.index_set(), \
                           self.model.F, \
                           "Incorrect set for 'x', expected: '" + \
                           str(self.model.F) + "', actual: '" + \
                           str(self.model.x_vars.index_set()) + "'")
        for f in self.model.F:
            self.assertEquals( self.model.x_vars[f].bounds, \
                               (None, None),
                               "Incorrect bounds for x[" + str(f) + "], expected: " + \
                               str((None, None)) + ", actual: " + \
                               str(self.model.x_vars[f].bounds) )
            
        self.assertEquals( self.model.u_vars.domain, NonNegativeReals, \
                           "Incorrect domain for 'u', expected: 'NonNegativeReals', actual: '" + str(self.model.u_vars.domain) + "'")
        self.assertEquals( self.model.u_vars.index_set(), \
                           self.model.S, \
                           "Incorrect set for 'u', expected: '" + \
                           str(self.model.S) + "', actual: '" + \
                           str(self.model.u_vars.index_set()) + "'")
        for s in self.model.S:
            self.assertEquals( self.model.u_vars[s].bounds, \
                               (0, None),
                               "Incorrect bounds for u[" + str(s) + "], expected: " + \
                               str((0, None)) + ", actual: " + \
                               str(self.model.u_vars[s].bounds) )

        self.assertEquals( len(self.model.L_var), 1, \
                           "Incorrect size for 'L', expected: 1, actual: " + str(len(self.model.L_var)) )
        self.assertEquals( self.model.L_var.domain, Reals, \
                           "Incorrect domain for 'L', expected: 'Reals', actual: '" + str(self.model.L_var.domain) + "'")
        self.assertEquals( self.model.L_var.bounds, (None, None), \
                           "Incorrect bounds for 'L', expected: '(None, None)', actual: '" + str(self.model.L_var.bounds) + "'")

    def test_parameters(self):
        self.assertEquals(value(self.model.h[None]), self.data.numberOfTimeIntervals, \
                          "Incorrect value for parameter 'h'" + 
                          ", expected: " + str(self.data.numberOfTimeIntervals) + 
                          ", actual: " + str(value(self.model.h[None])) )
        self.assertEquals(value(self.model.f[None]), self.data.numberOfForwardProducts, \
                          "Incorrect value for parameter 'f'" + 
                          ", expected: " + str(self.data.numberOfForwardProducts) + 
                          ", actual: " + str(value(self.model.f[None])) )
        self.assertEquals(value(self.model.s[None]), self.data.numberOfHpfcVectors, \
                          "Incorrect value for parameter 's'" + 
                          ", expected: " + str(self.data.numberOfHpfcVectors) + 
                          ", actual: " + str(value(self.model.s[None])) )
        self.assertEquals(value(self.model.T_param[None]), self.data.T, \
                          "Incorrect value for parameter 'T'" + 
                          ", expected: " + str(self.data.T) + 
                          ", actual: " + str(value(self.model.T_param[None])) )
        
        self.assertEquals((self.model.H.first(), self.model.H.last()), (1, 24), \
                          "Incorrect value for set 'H', expected: (1, 24), actual: " + str((self.model.H.first(), self.model.H.last())) )
        self.assertEquals((self.model.F.first(), self.model.F.last()), (1, 3), \
                          "Incorrect value for set 'F', expected: (1, 3), actual: " + str((self.model.F.first(), self.model.F.last())) )
        self.assertEquals((self.model.S.first(), self.model.S.last()), (1, 4), \
                          "Incorrect value for set 'S', expected: (1, 4), actual: " + str((self.model.S.first(), self.model.S.last())) )
        self.assertEquals((self.model.TH.first(), self.model.TH.last()), (1, 24), \
                          "Incorrect value for set 'TH', expected: (1, 24), actual: " + str((self.model.TH.first(), self.model.TH.last())) )


    def test_objective(self):
        Risk = "L_var + 1.25*( u_vars[1] + u_vars[2] + u_vars[3] + u_vars[4] )"
        self.assertEquals(str(self.model.Risk.expr), Risk, \
                          "Incorrect objective, expected:\n" + Risk + "\nactual:\n" + str(self.model.Risk.expr))

    def test_positivePart(self):
        PositivePartConstraint = ["47.83*( -12 + x_vars[1] + x_vars[2] ) + 44.83*( -8 + x_vars[1] + x_vars[2] ) + 42.23*( -10 + x_vars[1] + x_vars[2] ) + 38.97*( -7 + x_vars[1] + x_vars[2] ) + 36.72*( -7 + x_vars[1] + x_vars[2] ) + 38.26*( -13 + x_vars[1] + x_vars[2] ) + 31.53*( -8 + x_vars[1] + x_vars[2] ) + 31.02*( -18 + x_vars[1] + x_vars[2] ) + 39.41*( -21 + x_vars[1] + x_vars[3] ) + 43.73*( -23 + x_vars[1] + x_vars[3] ) + 46.06*( -21 + x_vars[1] + x_vars[3] ) + 49.94*( -17 + x_vars[1] + x_vars[3] ) + 50.84*( -19 + x_vars[1] + x_vars[3] ) + 45.11*( -19 + x_vars[1] + x_vars[3] ) + 43.07*( -17 + x_vars[1] + x_vars[3] ) + 41.7*( -20 + x_vars[1] + x_vars[3] ) + 41.22*( -23 + x_vars[1] + x_vars[3] ) + 47.87*( -17 + x_vars[1] + x_vars[3] ) + 60.92*( -23 + x_vars[1] + x_vars[3] ) + 63.93*( -14 + x_vars[1] + x_vars[3] ) + 61.07*( -12 + x_vars[1] + x_vars[2] ) + 54.9*( -8 + x_vars[1] + x_vars[2] ) + 60.03*( -13 + x_vars[1] + x_vars[2] ) + 52.81*( -7 + x_vars[1] + x_vars[2] ) - 24 * ( 1 + 0.01*x_vars[1] ) * x_vars[1] - 20 * ( 1 + 0.01*x_vars[2] ) * x_vars[2] - 20 * ( 1 + 0.01*x_vars[3] ) * x_vars[3] + L_var + u_vars[1]",
                                  "48.46*( -12 + x_vars[1] + x_vars[2] ) + 39.18*( -8 + x_vars[1] + x_vars[2] ) + 40.81*( -10 + x_vars[1] + x_vars[2] ) + 28.55*( -7 + x_vars[1] + x_vars[2] ) + 26.84*( -7 + x_vars[1] + x_vars[2] ) + 38.34*( -13 + x_vars[1] + x_vars[2] ) + 30.67*( -8 + x_vars[1] + x_vars[2] ) + 29.31*( -18 + x_vars[1] + x_vars[2] ) + 38.22*( -21 + x_vars[1] + x_vars[3] ) + 31.81*( -23 + x_vars[1] + x_vars[3] ) + 43.85*( -21 + x_vars[1] + x_vars[3] ) + 45.2*( -17 + x_vars[1] + x_vars[3] ) + 48.96*( -19 + x_vars[1] + x_vars[3] ) + 43.42*( -19 + x_vars[1] + x_vars[3] ) + 40.45*( -17 + x_vars[1] + x_vars[3] ) + 43.34*( -20 + x_vars[1] + x_vars[3] ) + 45.96*( -23 + x_vars[1] + x_vars[3] ) + 48.06*( -17 + x_vars[1] + x_vars[3] ) + 52.79*( -23 + x_vars[1] + x_vars[3] ) + 73.36*( -14 + x_vars[1] + x_vars[3] ) + 61.52*( -12 + x_vars[1] + x_vars[2] ) + 54.77*( -8 + x_vars[1] + x_vars[2] ) + 47.56*( -13 + x_vars[1] + x_vars[2] ) + 58.18*( -7 + x_vars[1] + x_vars[2] ) - 24 * ( 1 + 0.01*x_vars[1] ) * x_vars[1] - 20 * ( 1 + 0.01*x_vars[2] ) * x_vars[2] - 20 * ( 1 + 0.01*x_vars[3] ) * x_vars[3] + L_var + u_vars[2]",
                                  "47.43*( -12 + x_vars[1] + x_vars[2] ) + 32.61*( -8 + x_vars[1] + x_vars[2] ) + 37.54*( -10 + x_vars[1] + x_vars[2] ) + 36.11*( -7 + x_vars[1] + x_vars[2] ) + 27.36*( -7 + x_vars[1] + x_vars[2] ) + 39.31*( -13 + x_vars[1] + x_vars[2] ) + 30.2*( -8 + x_vars[1] + x_vars[2] ) + 25.45*( -18 + x_vars[1] + x_vars[2] ) + 47.2*( -21 + x_vars[1] + x_vars[3] ) + 37.18*( -23 + x_vars[1] + x_vars[3] ) + 59.8*( -21 + x_vars[1] + x_vars[3] ) + 44.01*( -17 + x_vars[1] + x_vars[3] ) + 45.81*( -19 + x_vars[1] + x_vars[3] ) + 46.01*( -19 + x_vars[1] + x_vars[3] ) + 37.87*( -17 + x_vars[1] + x_vars[3] ) + 46.8*( -20 + x_vars[1] + x_vars[3] ) + 48.58*( -23 + x_vars[1] + x_vars[3] ) + 54.67*( -17 + x_vars[1] + x_vars[3] ) + 60.11*( -23 + x_vars[1] + x_vars[3] ) + 71.95*( -14 + x_vars[1] + x_vars[3] ) + 72.62*( -12 + x_vars[1] + x_vars[2] ) + 49.59*( -8 + x_vars[1] + x_vars[2] ) + 50.99*( -13 + x_vars[1] + x_vars[2] ) + 47.87*( -7 + x_vars[1] + x_vars[2] ) - 24 * ( 1 + 0.01*x_vars[1] ) * x_vars[1] - 20 * ( 1 + 0.01*x_vars[2] ) * x_vars[2] - 20 * ( 1 + 0.01*x_vars[3] ) * x_vars[3] + L_var + u_vars[3]"]
        for f in range(3):
            self.assertEquals(str(self.model.PositivePartConstraint[f+1].body), PositivePartConstraint[f], \
                          "Incorrect positive part constraint '" + str(f+1) + \
                          "', expected:\n" + PositivePartConstraint[f] + \
                          "\nactual:\n" + str(self.model.PositivePartConstraint[f+1].body))

    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
