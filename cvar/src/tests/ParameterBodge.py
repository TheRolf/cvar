'''
Created on 16 May 2016

@author: Rolf
'''
from pyomo.environ import SolverFactory
from lib.excel.data import Data
from lib.pyomo.initialiser import Initialiser
from lib.excel.excel_reader import ExcelReader
from root import Root
from lib.excel.plotter import Plotter  # @UnusedImport
from pprint import pprint
import numpy
from matplotlib import pyplot
import os
from tools import Tools
from pyomo.opt.results.solver import SolverStatus, TerminationCondition

def main(test, solver, eps0):
    plot_folder = Root.resources() + "/parameter_bodge/" + "plots_" + test.split('.')[0]  + "_eps_" + str(eps0) + "_prices_1.0_" + solver + "_dist/faklya/"
    if not os.path.isdir(plot_folder):
        os.mkdir(plot_folder)
    if not os.path.exists(plot_folder):
        os.makedirs(plot_folder)
    
    data, wb = ExcelReader.read(Data(), Root.resources() + test)
    wb.save()
    wb.close()
    data.eps0 = eps0
    data.alpha = 1
    instance = Initialiser.init(data)
    res = []
        
    alphas = list(numpy.arange(0.05, 1, 0.1))
    for alpha in alphas:
        print alpha
        data.alpha = float(alpha)
        instance.alpha_param.set_value(data.alpha)
        instance.name = data.name + "_a" + str(data.alpha) + "_e" + str(data.eps0) + "_s" + str(data.numberOfHpfcVectors)
        #instance.alpha_param.construct()
        #instance.Risk.construct()
        
        if solver == "xpress":
            opt = SolverFactory("asl", executable="xpress")
            opt.options["logfile"] = plot_folder + "xpress_log.txt"
        elif solver == "gurobi":
            opt = SolverFactory("gurobi")
            opt.options["Logfile"] = plot_folder + "gurobi_log.txt"
            opt.options["TimeLimit"] = 15
            
        Tools.Logger(plot_folder + solver + "_log.txt", instance.name)
        
        result = opt.solve(instance)
        
        #instance.write(Root.resources() + '/parameter_bodge/problem.lp', io_options={'symbolic_solver_labels':True})
        
        if (result.solver.status == SolverStatus.ok or result.solver.status == SolverStatus.warning) and (result.solver.termination_condition != TerminationCondition.unbounded and result.solver.termination_condition != TerminationCondition.infeasible):  # @UndefinedVariable
            instance.solutions.load_from(result)
        
            #print result.solver.status, result.solver.termination_condition
            #print "VaR:  ", instance.L_var()
            #print "CVaR: ", instance.Risk()
            res.append( (alpha, instance.L_var()/1000, instance.Risk()/1000) )
            plot = Plotter.plotTotalEnergy(data, instance)
            plot.savefig(plot_folder + str(alpha) + ".png")
            plot.close()
        else:
            res.append( (alpha, None, None) )
    
    print test, solver, eps0
    pprint(res, open(plot_folder + "res.txt", 'w'), width=200)
    
    ax = pyplot.gca()
    ax.ticklabel_format(useOffset=False)
    
    pyplot.plot(alphas, [r[1] for r in res], alphas, [r[2] for r in res])

    pyplot.savefig(plot_folder + "/alpha_var+cvar.png")
    pyplot.close()

def main2(test, solver, eps0, res):
    plot_folder = Root.resources() + "/parameter_bodge/" + "plots_" + test.split('.')[0]  + "_eps_" + str(eps0) + "_prices_1.0_" + solver + "_dist/"

    alphas = list(numpy.arange(0.05, 1, 0.1))

    ax = pyplot.gca()
    ax.ticklabel_format(useOffset=False)
    
    pyplot.plot(alphas, [r[1] for r in res], alphas, [r[2] for r in res])

    pyplot.savefig(plot_folder + "/alpha_var+cvar.png")
    pyplot.close()

if __name__ == '__main__':
    #main('test2.xlsm', "gurobi", 0.005)
    #main('test2.xlsm', "xpress", 0.005)
    #main('test4.xlsm', "gurobi", 0.001)
    main('test4.xlsm', "xpress", 0.001)
    #main2('test4.xlsm', "gurobi", 0.001)
        
    pass    