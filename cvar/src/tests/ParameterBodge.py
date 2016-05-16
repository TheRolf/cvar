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

if __name__ == '__main__':
    data, wb = ExcelReader.read(Data(), Root.resources() + 'test2.xlsm')
    wb.save()
    data.epsilon0 = 0.01
    #data.alpha = 0.8
    res = []
    plot_folder = Root.resources() + "/parameter_bodge/" + "plots_test2_eps_" + str(data.epsilon0) + "_prices_0.9/"
    if not os.path.exists(plot_folder):
        os.makedirs(plot_folder)
    alphas = list(numpy.arange(0.05, 1, 0.05))
    for alpha in []:#alphas:
        print alpha
        data.alpha = float(alpha)
        
        model = Initialiser.init(data)
        
        opt = SolverFactory("gurobi")
        f = open(Root.resources() + "/parameter_bodge/gurobi_log_acc.txt", "a+")
        f.write( open(Root.resources() + "/parameter_bodge/gurobi_log_new.txt", "a+").read() )
        f.close()
        open(Root.resources() + "/parameter_bodge/gurobi_log_new.txt", 'w').close()
        opt.options["LogFile"] = Root.resources() + "/parameter_bodge/gurobi_log_new.txt"
        model.write(Root.resources() + '/parameter_bodge/problem.lp', io_options={'symbolic_solver_labels':True})
        
        result = opt.solve(model)
        model.solutions.load_from(result)
        
        #print result.solver.status, result.solver.termination_condition
        #print "VaR:  ", model.L_var()
        #print "CVaR: ", model.Risk()
        #for s in model.S:
        #    print s, model.u_vars[s]()
        if alpha != 0.2 and model.Risk():
            res.append( (alpha, model.L_var()/1000, model.Risk()/1000) )
            #Plotter.plotTotalEnergy(data, model).show()
            plot = Plotter.plotTotalEnergy(data, model)
            plot.savefig(plot_folder + str(alpha) + ".png")
            plot.close()
    
    pprint(res)
    
    ax = pyplot.gca()
    ax.ticklabel_format(useOffset=False)
    
    pyplot.plot(alphas, [r[1] for r in res], alphas, [r[2] for r in res])
    '''
    res = [(0.050000000000000003, 25449.0379779, 25466.59304434484),
 (0.10000000000000001, 25468.343722600002, 25476.544672410742),
 (0.15000000000000002, 25469.6416153, 25477.004997324664),
 (0.2, None, None),
 (0.25, 25469.5661454, 25477.862654491015),
 (0.29999999999999999, 25471.8245139, 25479.696365464737),
 (0.35000000000000003, 25477.884628800002, 25484.190991158244),
 (0.40000000000000002, 25475.6415719, 25483.614577433862),
 (0.45000000000000001, 25474.9359488, 25481.008531293846),
 (0.5, 25480.678611400002, 25484.83313930074),
 (0.55000000000000004, 25478.2695203, 25480.952223760058),
 (0.60000000000000009, 25476.657701, 25480.832523008587),
 (0.65000000000000013, 25481.001816, 25496.482997512583),
 (0.70000000000000007, 25481.0651139, 25482.39283002141),
 (0.75000000000000011, 25481.1272494, 25482.532146567457),
 (0.80000000000000004, 25480.9662407, 25482.623924919233),
 (0.85000000000000009, 25492.8987338, 25494.573397619366),
 (0.90000000000000013, 25484.1761085, 25484.179969041503),
 (0.95000000000000007, 25484.1793479, 25484.179348419075)]
    pyplot.plot([r[0] for r in res], [r[1] for r in res], [r[0] for r in res], [r[2] for r in res])
    '''
    pyplot.savefig(plot_folder + "/alpha_var+cvar.png")
