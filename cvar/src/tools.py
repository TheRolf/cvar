'''
Created on 31 Mar 2016

@author: Rolf
'''
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
            
    class OutOfHedgingPeriodException(Exception):
        pass
    
    class EpsilonIsZeroException(Exception):
        pass

    Debug = False