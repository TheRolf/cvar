'''
Created on 24 Mar 2016

@author: Rolf
'''
from xlwings import Workbook
from lib.excel.excel_reader_functions import ExcelReaderFunctions

class ExcelReader(object):

    @staticmethod
    def read(*args):
        data = args[0]
        if len(args) == 1:
            wb = Workbook.caller()
        elif len(args) == 2:
            filename = args[1]
            wb = Workbook(filename)
        else:
            return None
        
        data.alpha = ExcelReaderFunctions.importAlpha()
        data.epsilon0 = ExcelReaderFunctions.importEpsilon()
        data.T = ExcelReaderFunctions.importT()
       
        data.demand, data.numberOfTimeIntervals, data.demandAsArray = ExcelReaderFunctions.importDemand()
        data.forwardCharVectors, data.numberOfForwardProducts = ExcelReaderFunctions.importForwardCharVectors()
        data.hpfcVectors, data.numberOfHpfcVectors = ExcelReaderFunctions.importHpfcVectors()
        data.forwardPrices = ExcelReaderFunctions.importForwardPrices()
        
        data.hedgingPeriodNames = ExcelReaderFunctions.importHedgingPeriodNames()
        data.forwardProductNames = ExcelReaderFunctions.importForwardProductNames()
        if len(args) == 2:
            #wb.close()
            pass
        
        return data, wb  
        