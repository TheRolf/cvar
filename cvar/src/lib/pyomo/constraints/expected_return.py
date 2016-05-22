'''
Created on 28 Apr 2016

@author: Rolf
'''
from pyomo.core.base.constraint import Constraint
from numpy import mean

class ExpectedReturn(object):

    @staticmethod
    def add(model):
        def mean_of_hpfc(model, t):
            return mean([model.y_params[s,t] for s in model.S])
        
        def V1():
            return sum( (1 + model.eps0_param*model.x_vars[f])*model.P0_params[f]*model.x_vars[f] \
                        for f in model.F )
        def VT():
            return sum(  mean_of_hpfc(model, t)*(sum( model.A_params[f,t]*model.x_vars[f] for f in model.F ) - model.D_params[t])\
                        for t in model.TH )
        
        def exp_ret_rule(model):
            return VT() - V1() >= 1220
        
        model.ExpectedReturnConstraint = Constraint(rule=exp_ret_rule)
        
        return model