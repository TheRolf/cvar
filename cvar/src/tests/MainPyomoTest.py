'''
Created on 10 Apr 2016

@author: Rolf
'''
import unittest

from pyomo.opt.results.solver import SolverStatus, TerminationCondition

from lib.pyomo.main_pyomo import MainPyomo

class Test(unittest.TestCase):


    def test_mainPyomo(self):
        model, result = MainPyomo.main('/../resources/test0.xlsm')[:-1]
        self.assertEquals(result.solver.status, SolverStatus.ok, \
                          "Incorrect solver status: '" + str(result.solver.status) + "', should be '" + str(SolverStatus.ok) + "'")
        # a kov. sorokra hibat ir, de lefut
        self.assertEquals(result.solver.termination_condition, TerminationCondition.optimal, "Incorrect solver termination condition: '" + str(result.solver.termination_condition ) + "', should be '" + str(TerminationCondition.optimal) + "'")  # @UndefinedVariable
        x_vars = [8.86723027681, 3.63727102944, 14.5836973611]
        risk = 14128.1976751
        for f in range(model.f()):
            # TODO: 3. tizedesjegyben mar nem egyezik
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