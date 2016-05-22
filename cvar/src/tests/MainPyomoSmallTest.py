'''
Created on 10 Apr 2016

@author: Rolf
'''
import unittest

from pyomo.opt.results.solver import SolverStatus, TerminationCondition

from lib.pyomo.main_pyomo import MainPyomo
from lib.pyomo.constraints.positive_part import PositivePart

class Test(unittest.TestCase):


    def test_mainPyomoSmall(self):
        PositivePart.X = True
        model, result = MainPyomo.main('/../resources/test0.xlsm')[:-1]
        self.assertEquals(result.solver.status, SolverStatus.ok, \
                          "Incorrect solver status: '" + str(result.solver.status) + "', should be '" + str(SolverStatus.ok) + "'")
        self.assertEquals(result.solver.termination_condition, TerminationCondition.optimal, "Incorrect solver termination condition: '" + str(result.solver.termination_condition ) + "', should be '" + str(TerminationCondition.optimal) + "'")  # @UndefinedVariable
        x_vars = [8.16248754389, 2.59396693762, 14.2582355634]
        risk = 14292.1616
        for f in range(model.f()):
            self.assertAlmostEquals(model.x_vars[f+1](), x_vars[f], places = 2, \
                                    msg = "Incorrect solution, x" + str(f+1) + " = " + 
                                    str(model.x_vars[f+1]()) + ", should be " + str(x_vars[f]))
        self.assertAlmostEquals(model.Risk(), risk, places = 2, \
                                msg = "Incorrect objective value: " + 
                                str(model.Risk()) + ", should be " + str(risk) )

        #print [value(item) for i, item in model.x_vars.items()]
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()