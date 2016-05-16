'''
Created on 31 Mar 2016

@author: Rolf
'''
from xlwings.main import Range

from tools import Tools

class ExcelReaderFunctions(object):

    @staticmethod
    def importForwardCharVectors():
        fcvTemp = Range("forward", "B3").options(transpose=True).table.value
        for i in range(len(fcvTemp)):
            for j in range(len(fcvTemp[0])):
                fcvTemp[i][j] = int(fcvTemp[i][j])
        return Tools.ListToDict2D(fcvTemp), len(fcvTemp)
    
    @staticmethod
    def importHpfcVectors():
        hvTemp = Range("hpfc", "B2").options(transpose=True).table.value
        for i in range(len(hvTemp)):
            for j in range(len(hvTemp[0])):
                hvTemp[i][j] = hvTemp[i][j]
        return Tools.ListToDict2D(hvTemp), len(hvTemp)
    
    @staticmethod
    def importDemand():
        dTemp = Range("demand", "B2").table.value
        return Tools.ListToDict1D(dTemp), len(dTemp), dTemp
    
    @staticmethod
    def importForwardPrices():
        fpTemp = Range("forward", "B2").horizontal.value
        return Tools.ListToDict1D(fpTemp)
    
    @staticmethod
    def importAlpha():
        return Range("parameters", "B1").value
    
    @staticmethod
    def importEpsilon():
        return Range("parameters", "B2").value
    
    @staticmethod
    def importHedgingPeriodNames():
        return Range("demand", "A2").vertical.value
    
    @staticmethod
    def importForwardProductNames():
        return Range("forward", "B1").horizontal.value