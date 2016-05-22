'''
Created on 25 Apr 2016

@author: Rolf
'''

from lib.excel.plotter import Plotter
from root import Root
from lib.pyomo.constraints.positive_part import PositivePart
from lib.excel.data import Data
from lib.excel.excel_reader import ExcelReader
from lib.pyomo.initialiser import Initialiser
from pyomo.environ import SolverFactory
from tools import Tools

    
def main():
    Tools.Debug = False
    e0_vec = [0.002, 0.001, 0.0005]
    for n in [1, 3]:
        if n==1:
            testname = '/../resources/test3_10.xlsm'
        elif n==3:
            testname = '/../resources/test2_10.xlsm'
        data, wb = ExcelReader.read(Data(), Root.path() + testname)
        for e0 in e0_vec:
            for X in [True, False]:
                PositivePart.X = X
                if X:
                    x=2
                else:
                    x=1                 
                data.eps0 = e0
                model = Initialiser.init(data)
                
                opt = SolverFactory("asl", executable="xpress")
                opt.options["logfile"] = Root.resources() + "xpress_log.txt"
                Tools.Logger(Root.resources() + "xpress_log.txt", model.name)
                print model.name, e0, X
                results = opt.solve(model)
                model.solutions.load_from(results)
                filename = "c:/Users/Rolf/Desktop/BME/Workspace/Diplomamunka/cikk/figures" + str(x) + "/" + str(n) + "month_0.8_" + str(e0) + ".png"
                plot = Plotter.plotTotalEnergy(data, model)
                plot.savefig(filename)
                plot.close()
                
        wb.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    main()