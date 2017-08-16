# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 22:31:44 2017

The function doSomeIntegrals() contains examples of integrating some single-variable functions.

The function verifykSigmaHeuristic() verifies the 68-95-99.7 rule by running a simulation.
"""
from scipy.integrate import quad #quadrature method of integration
from math import sqrt 
import random 


def doSomeIntegrals():
    #integrate 3x^2+2*sqrt(x)+3*x^(1/3) over x in (0,1)
    f = lambda x:3*x**2+2*sqrt(x)+3*x**(1/3) 
    print(quad(f, 0, 1)[0]) #Answer should be approx 4.583 (Problem 5.5.1 in Edwards and Penney, Calculus, 6e).
    
    #Note, scippy.integrate.quad returns a tuple, the first element of which is the actual value of the definite integral.
    
    #integrate (x^2-1)/(sqrt(x)) over x in (1,4)
    f = lambda x: (x**2 - 1)/sqrt(x)
    print(quad(f, 1, 4)[0]) #Answer should be 52/5 (Problem 5.5.25 in Edwards and Penney, Calculus, 6e)
    
    #integrate x^99 over x in (-1,1)
    f = lambda x: x**99
    print(quad(f, -1, 1)[0]) #A Answer should be 0. (Problem 5.5.13 in Edwards and Penney, Calculus, 6e)
    
    #integrate sqrt(x) - 2/sqrt(x) over x in (1,9)
    f = lambda x: sqrt(x) - 2/sqrt(x)
    print(quad(f, 1, 9)[0]) #Answer should be 28/3


def verifykSigmaHeuristic():
    '''
    for various means and standard deviations, verifies
    that ~68% of gaussian random variables are within 1 standard deviation from the mean,
    that ~95% of gaussian random variables are within 1.96 standard deviations from the mean,
    and that ~99.7% of gaussian random variables are within 3 standard deviations
    
    
    '''
    means = tuple(range(-8, 8))
    stdevs = tuple([0.5*i for i in range(1,6)])
    oneSigmaCt, twoSigmaCt, threeSigmaCt = 0, 0, 0
    numTrialsForEachMnStdev = 10000
    for mn in means:
        for stdev in stdevs:
            for trial in range(numTrialsForEachMnStdev): #within 1 stdev of mean
                g = random.gauss(mn, stdev)
                if mn - stdev<= g <= mn + stdev:
                    oneSigmaCt+=1
                elif mn - 1.96 * stdev <= g <= mn + 1.96 * stdev: #btwn 1 and 2 stdevs from mean
                    twoSigmaCt+=1
                elif mn - 3 * stdev <= g <= mn + 3 * stdev: #btwn 2 and 3 stdevs from mean
                    threeSigmaCt+=1
                    
    totTrials = len(means) * len(stdevs) * numTrialsForEachMnStdev
    print("Fraction within 1 standard deviation of mean:"+str(oneSigmaCt/totTrials))
    print("Fraction within 2 standard deviations of mean:"+str((oneSigmaCt+twoSigmaCt)/totTrials))
    print("Fraction within 3 standard deviations of mean:"+str((oneSigmaCt+twoSigmaCt+threeSigmaCt)/totTrials))

if __name__ == "__main__":
    verifykSigmaHeuristic()
    

