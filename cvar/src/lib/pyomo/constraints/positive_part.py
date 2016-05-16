'''
Created on 29 Mar 2016

@author: Rolf
'''
from pyomo.core.base.constraint import Constraint

class PositivePart(object):
    
    X = True
    
    @staticmethod
    def add(model):
        def V1():
            return sum( (1 + model.epsilon_param*model.x_vars[f])*model.P0_params[f]*model.x_vars[f] \
                        for f in model.F )
            
            #return sum( (1 + model.epsilon_param*sqrt(model.x_vars[f]))*model.P0_params[f]*model.x_vars[f] \
            #            for f in model.F )
        def VT(s):
            #X = True
            if PositivePart.X:
                return sum( (1 - model.epsilon_param*(sum( model.A_params[f,t]*model.x_vars[f] for f in model.F ) - model.D_params[t]))*model.y_params[s,t]*(sum( model.A_params[f,t]*model.x_vars[f] for f in model.F ) - model.D_params[t])\
                            for t in model.H )
            
            else:
                return sum( model.y_params[s,t]*(sum( model.A_params[f,t]*model.x_vars[f] for f in model.F ) - model.D_params[t])\
                            for t in model.H )
      

        
        def pos_part_rule(model, s):
            return VT(s) - V1() + model.L_var + model.u_vars[s] >= 0
        
        model.PositivePartConstraint = Constraint(model.S, rule=pos_part_rule)    
        
        return model