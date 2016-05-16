'''
Created on 30 Mar 2016

@author: Rolf
'''

from time import time

from pyomo.environ import SolverFactory

from lib.excel.data import Data
from lib.excel.excel_reader import ExcelReader
from lib.excel.excel_writer import ExcelWriter
from lib.pyomo.initialiser import Initialiser
from root import Root
from tools import Tools
from lib.excel.plotter import Plotter
from pyutilib.common import ApplicationError  # @UnresolvedImport

class MainPyomo(object):

    @staticmethod
    def main(*args):
        t0 =  time()
        # EXCEL-bol hivva
        if len(args) == 0:
            data = ExcelReader.read(Data())[0]
            ExcelWriter.clear(data)
        # ECLIPSE-bol hivva
        elif len(args) == 1:
            filename = args[0]
            data, wb = ExcelReader.read(Data(), Root.path() + filename)
        
        t1 = time()
        if len(args)==0:
            ExcelWriter.excelTime(t1-t0)
        
        model = Initialiser.init(data)
        opt = SolverFactory("gurobi")
        opt.options["LogFile"] = Root.resources() + "gurobi_log.txt"
        
        t2 = time()
        if len(args)==0:
            ExcelWriter.pyomoTime(t2-t1)
        
        if Tools.Debug:
            model.write(Root.resources() + 'problem.lp', io_options={'symbolic_solver_labels':True})

        results = opt.solve(model)
        
        try:
            pass
        except Exception as e:
            if type(e) == ZeroDivisionError:
                ExcelWriter.exception("Division by zero: 'alpha' should be < 1.")
            elif type(e) == Tools.OutOfHedgingPeriodException:
                ExcelWriter.exception("Empty planning horizon: T should be no more than the number of time periods.")
            elif type(e) == Tools.EpsilonIsZeroException:
                ExcelWriter.exception("Unbounded problem: epsilon should not equal 0.")
            elif type(e) == ApplicationError:
                ExcelWriter.exception("Unfeasible problem.")
            traceback.format_exc()  # @UndefinedVariable

                #ExcelWriter.exception("Unhandled exception:", e)
            return
        

        model.solutions.load_from(results)
        t3 = time()
        if len(args)==0:
            ExcelWriter.gurobiTime(t3-t2)
        
        if Tools.Debug:
            print "Excel read:  {0:0.3f} seconds".format(t1-t0)
            print "Model build: {0:0.3f} seconds".format(t2-t1)
            print "Solve:       {0:0.3f} seconds".format(t3-t2)
        
        if len(args) == 0:
            if Tools.Debug:
                f = open(Root.resources() + "/yxc.txt", 'w')
                print >>f, results
                Plotter.plotTotalEnergy(data, model).show()
            ExcelWriter.write(model, results)
            
        elif len(args) == 1:
            wb.close()
            return (model, results, data)
        
if __name__ == '__main__':
    print "Calling MainPyomo.main() from main_pyomo.py"
    #model, result = MainPyomo.main('/../resources/test0.xlsm')


