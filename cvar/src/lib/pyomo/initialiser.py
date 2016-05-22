'''
Created on 29 Mar 2016

@author: Rolf
'''

from pyomo.core.base.PyomoModel import AbstractModel

from lib.pyomo.constraints.positive_part import PositivePart
from lib.pyomo.objective import Objective
from lib.pyomo.parameters import Parameters
from lib.pyomo.variables import Variables

from tools import Tools

#from lib.pyomo.constraints.expected_return import ExpectedReturn
class Initialiser(object):

    @staticmethod
    def init(data):
        data.initialise()
        #logfile = open(Root.resources() + "logfile.txt", 'w')
        #t0 = time()
        name = data.name + "_a" + str(data.alpha) + "_e" + str(data.eps0) + "_s" + str(data.numberOfHpfcVectors)
        model = AbstractModel(name=name)
        #t1 = time()
        #logfile.write("AbstractModel()\n\t" + "{0:0.9f}\n".format(t1-t0))
        model = Parameters.add(model, data)
        #t2 = time()
        #logfile.write("Parameters\n\t" + "{0:0.9f}\n".format(t2-t1))
        model = Variables.add(model)
        #t3 = time()
        #logfile.write("Variables\n\t" + "{0:0.9f}\n".format(t3-t2))        
        model = Objective.add(model)
        #t4 = time()
        #logfile.write("Objective\n\t" + "{0:0.9f}\n".format(t4-t3))        
        model = PositivePart.add(model)
        #t5 = time()
        #logfile.write("PositivePart\n\t" + "{0:0.9f}\n".format(t5-t4))             
        #model = ExpectedReturn.add(model)
        instance = model.create_instance(data=data.dictionary, report_timing=Tools.Debug)
        return instance
        #t6 = time()
        #logfile.write("Construct\n\t" + "{0:0.9f}\n".format(t6-t5))     
        
