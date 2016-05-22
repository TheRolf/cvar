'''
Created on 31 Mar 2016

@author: Rolf
'''
import os
from time import strftime
import datetime

class Tools(object):

    @staticmethod
    def ListToDict1D(arr):
        return dict((i+1, arr[i]) for i in range(len(arr)))

    @staticmethod
    def ListToDict2D(arr):
        return dict(((i+1,j+1), arr[i][j]) for i in range(len(arr)) for j in range(len(arr[0])))
    
    @staticmethod
    def Transpose(arr):
        return list(map(list, zip(*arr)))

    @staticmethod
    def Logger(filepath, modelname):
        newLogPath = filepath
        allLogPath = filepath.replace(".txt", "_all.txt")
        if os.path.isfile(newLogPath):
            newLogFile = open(newLogPath, "r")
            allLogFile = open(allLogPath, "a+")
            
            # append the content of the logfile to the "all" logfile
            allLogFile.write( newLogFile.read() )
            newLogFile.close()
            allLogFile.close()
        
        # clearing the logfile and writing the model name on top
        newLogFile = open(newLogPath, "w")
        newLogFile.write("\n\n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        newLogFile.write("\n" + modelname)
        newLogFile.close()
        return
            
    class OutOfHedgingPeriodException(Exception):
        pass
    
    class EpsilonIsZeroException(Exception):
        pass

    Debug = True