'''
Created on 29 Mar 2016

@author: Rolf
'''

from pyomo.core import Param
from pyomo.core.base.rangeset import RangeSet
from pyomo.core.base.set_types import NonNegativeIntegers, NonNegativeReals, \
    Reals, Binary
from tools import Tools

class Parameters(object):
    
    @staticmethod
    def add(model, data):
        if data.T > data.numberOfTimeIntervals:
            raise Tools.OutOfHedgingPeriodException
#         if data.epsilon0 == 0:
#             raise Tools.EpsilonIsZeroException
            pass
        
        model.h = Param(domain=NonNegativeIntegers, initialize=data.numberOfTimeIntervals)
        model.f = Param(domain=NonNegativeIntegers, initialize=data.numberOfForwardProducts)
        model.s = Param(domain=NonNegativeIntegers, initialize=data.numberOfHpfcVectors)
        
        # set H: hedging period
        model.H = RangeSet(1, model.h)
        # set F: forward and spot products
        model.F = RangeSet(1, model.f)
        # set S: scenarios
        model.S = RangeSet(1, model.s)
            
        # D[t]:    energy demand for time period 't'
        model.D_params = Param(model.H, initialize=data.demand)
        # A[f,t]:  availability of product 'f' for time period 't'  
        model.A_params = Param(model.F, model.H, domain=Binary, initialize=data.forwardCharVectors)
        # P0[f]:   initial price of product 'f'
        model.P0_params = Param(model.F, initialize=data.forwardPrices)
        
        # e0:      price correction coefficient
        model.epsilon_param = Param(domain=NonNegativeReals, initialize=data.epsilon0)
        # y[s,t]:  HPFC for scenario 's'
        model.y_params = Param(model.S, model.H, domain=Reals, initialize=data.hpfcVectors)
        # alpha:   significance level
        model.alpha_param = Param(domain=NonNegativeReals, initialize=data.alpha)
        
        model.T_param = Param(domain=NonNegativeIntegers, initialize=data.T)
        # set T: planning horizon
        model.TH = RangeSet(model.T_param+1, model.h)
        return model
    
