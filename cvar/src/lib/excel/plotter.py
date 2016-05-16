'''
Created on 25 Apr 2016

@author: Rolf
'''
from matplotlib import pyplot
from pyomo.core.base.numvalue import value

class Plotter(object):

    @staticmethod
    def plotTotalEnergy(data, model):
        x = [value(item) for i, item in model.x_vars.items()]  # @UnusedVariable
        energyFromProducts = [0] * data.numberOfTimeIntervals

        for t in range(data.numberOfTimeIntervals):
            for f in range(data.numberOfForwardProducts):
                energyFromProducts[t] += x[f]*data.forwardCharVectors[f+1, t+1]
        
        s = 18
        #ax = pyplot.subplots()[1]
        #ax.set_prop_cycle(cycler('color', ['b', 'r']))

        pyplot.figure(1, figsize=(10, 5))
        pyplot.subplots_adjust(bottom=0.3)

        pyplot.plot(data.hedgingPeriodNames, data.demandAsArray, 'b',
                    data.hedgingPeriodNames, energyFromProducts, 'r')
        pyplot.xticks(fontsize=s, rotation=45)
        pyplot.yticks(fontsize=s) 
        
        return pyplot
        