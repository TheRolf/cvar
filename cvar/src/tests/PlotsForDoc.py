'''
Created on 25 Apr 2016

@author: Rolf
'''

import unittest
from lib.excel.plotter import Plotter
from root import Root
from lib.pyomo.constraints.positive_part import PositivePart
from lib.excel.data import Data
from lib.excel.excel_reader import ExcelReader
from lib.pyomo.initialiser import Initialiser
from pyomo.environ import SolverFactory

class TestPlotsForDoc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #self.model, self.result, self.data = MainPyomo.main('/../resources/test3.xlsm')
        pass
    
    def test_plots(self):
        if False:
            e0_vec = [0.002, 0.001, 0.0005]
            for n in [1, 3]:
                if n==1:
                    testname = '/../resources/test3.xlsm'
                elif n==3:
                    testname = '/../resources/test2.xlsm'
                data, wb = ExcelReader.read(Data(), Root.path() + testname)
                for e0 in e0_vec:
                    for X in [True, False]:
                        PositivePart.X = X
                        if X:
                            x=2
                        else:
                            x=1                 
                        data.epsilon0 = e0
                        model = Initialiser.init(data)
                        opt = SolverFactory("gurobi")
                        results = opt.solve(model)
                        model.solutions.load_from(results)
                        filename = "/../../cikk/figures" + str(x) + "/" + str(n) + "month_0.8_" + str(e0) + ".png"
                        Plotter.plotTotalEnergy(data, model).savefig(Root.resources() + filename)
                        wb.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()