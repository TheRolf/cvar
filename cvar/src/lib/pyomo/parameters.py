'''
Created on 29 Mar 2016

@author: Rolf
'''

from pyomo.core import Param
from pyomo.core.base.rangeset import RangeSet
from pyomo.core.base.set_types import NonNegativeIntegers, NonNegativeReals, \
    Reals, Binary

class Parameters(object):
    
    @staticmethod
    def add(model, data):
        model.t = Param(domain=NonNegativeIntegers)
        model.f = Param(domain=NonNegativeIntegers)
        model.s = Param(domain=NonNegativeIntegers)
        
        # set T: hedging period
        model.T = RangeSet(1, model.t)
        # set F: forward and spot products
        model.F = RangeSet(1, model.f)
        # set S: scenarios
        model.S = RangeSet(1, model.s)
        
        # D[t]:    energy demand for time period 't'
        model.D_params = Param(model.T)
        # A[f,t]:  availability of product 'f' for time period 't'  
        model.A_params = Param(model.F, model.T, domain=Binary)
        # P0[f]:   initial price of product 'f'
        model.P0_params = Param(model.F)
        
        # e0:      price correction coefficient
        model.eps0_param = Param(domain=NonNegativeReals)
        # y[s,t]:  HPFC for scenario 's'
        model.y_params = Param(model.S, model.T, domain=Reals)
        # alpha:   significance level
        model.alpha_param = Param(domain=NonNegativeReals, mutable=True)

        return model
    
