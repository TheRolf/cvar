'''
Created on 29 Mar 2016

@author: Rolf
'''

from pyomo.core.base.objective import Objective as Obj
from pyomo.core.base.objective import minimize


class Objective(object):
   
    @staticmethod
    def add(model):
        def risk(model):
            return model.L_var + 1/((1-model.alpha_param)*model.s) * sum(model.u_vars[s] for s in model.S)
        model.Risk = Obj(rule=risk, sense=minimize)
        
        return model