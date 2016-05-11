'''
Created on 29 Mar 2016

@author: Rolf
'''
from pyomo.core.base.set_types import Reals, NonNegativeReals
from pyomo.core.base.var import Var


class Variables(object):

    @staticmethod
    def add(model):
        # x[f]: bought/sold amount of product 'f'
        model.x_vars = Var(model.F, domain=Reals)
        # u[s]: nonnegative dummy variable, for each scenario 's'
        model.u_vars = Var(model.S, domain=NonNegativeReals)
        # L:    VaR of the risk
        model.L_var = Var(domain=Reals)
        
        return model