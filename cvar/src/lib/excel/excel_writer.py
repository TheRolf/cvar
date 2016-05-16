'''
Created on 13 Apr 2016

@author: Rolf
'''
from xlwings.main import Sheet, Range

class ExcelWriter(object):

    @staticmethod
    def excelTime(time):
        Range((9, 1)).value = "Excel read time:"
        Range((9, 2)).value = "{0:0.2f}".format(time) + " seconds"

    @staticmethod
    def pyomoTime(time):
        Range((10, 1)).value = "Pyomo build time:"
        Range((10, 2)).value = "{0:0.2f}".format(time) + " seconds"
        
    @staticmethod
    def gurobiTime(time):
        Range((11, 1)).value = "Gurobi solve time:"
        Range((11, 2)).value = "{0:0.2f}".format(time) + " seconds"
        
    @staticmethod
    def write(model, result):
        Sheet("parameters").activate()
        Range((7,1)).value = "VaR"
        Range((8,1)).value = model.L_var()
        for f in model.F:
            Range((7, f+1)).value = "x[" + str(f) + "]"
            Range((8, f+1)).value = model.x_vars[f]()    

    
    @staticmethod
    def clear(data):
        Sheet("parameters").activate()
        for i in range(2):
            for j in range(data.numberOfForwardProducts+1):
                Range((7+i, 1+j)).value = ""
        for i in range(3):
            for j in range(2):
                Range((9+i,1+j)).value=""
    
    @staticmethod
    def exception(msg, exc=None):
        Sheet("parameters").activate()
        Range("A7").value = msg
        if exc:
            Range("B7").value = str(type(exc))
            Range("B8").value = str(exc)