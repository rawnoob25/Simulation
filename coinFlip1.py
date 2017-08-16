"""
Created on Fri Aug 11 18:39:24 2017

Simulates 10000 sets of 100 coinflips. Each set 
of 100 coinflips returns a point estimate of the probability 
of heads and the associated estimate of the standard error (using sample size 100).
A sampling distribution of 10,000 samples proportions is created. 

The standard deviation of the sampling distribution of 10,000 point estimates of the probability
of heads (sample size = 100) is compared to the theoretical standard deviation sqrt(((p)*(1-p))/n)
with p=0.5.
"""


import random, math
from statistics import mean, stdev
import pylab as plt

def flipSim(numTrials):
    l = ["H", "T"]
    def flip(numFlips):
        """
        Returns a point estimate of the 
        probability of a coinflip resulting in heads (using sample of
        size numFlips) along with the corresponding estimate
        of the standard error of the sampling distribution of
        this probability.
        """
        ct = 0
        for i in range(numFlips):
            if random.choice(l)== "H":
                ct+=1
        p_hat = ct/float(numFlips)
        return (p_hat, math.sqrt((p_hat*(1-p_hat))/numFlips))
    coinFlips = []
    for i in range(numTrials):
        coinFlips.append(flip(100)[0])
    print("The center of the distr flip(100) is:"+str(mean(coinFlips)))
    print("The standard deviation of the distr. flip(100) is:"+str(stdev(coinFlips)))




def illustrateRegressionToMean(numTrials, numStdDevsToQualityAsExtreme = 2):
    l = ["H", "T"]
    extreme = lambda p_hat, n:True if (p_hat>0.5+numStdDevsToQualityAsExtreme*math.sqrt(0.25/n) or p_hat<0.5-numStdDevsToQualityAsExtreme*math.sqrt(0.25/n)) else False
    def flip(numFlips):
        ct = 0
        for i in range(numFlips):
            if random.choice(l)== "H":
                ct+=1
        p_hat = ct/float(numFlips)
        return p_hat
    
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(10))
    
    extremeSetsOf10Flips = [] 
    followExtremes=[]
    for i in range(len(fracHeads) - 1):
        curr = fracHeads[i]
        if extreme(curr, 10):
            extremeSetsOf10Flips.append(curr)
            followExtremes.append(fracHeads[i+1])
    plt.plot(range(len(extremeSetsOf10Flips)), extremeSetsOf10Flips, 'bo', label = "extreme sets of 10 flips")
    plt.plot(range(len(extremeSetsOf10Flips)), followExtremes, 'r^', label = "Set of 10 flips following an extereme set")
    plt.ylim(0, 1)
    plt.xlim(-1, len(extremeSetsOf10Flips) + 1)
    plt.xlabel("Extreme and next trial")
    plt.ylabel("Fraction heads")
    plt.title("Illustrating regression to the mean with "+str(numTrials)+" trials and\n extreme boundary set at "+str(numStdDevsToQualityAsExtreme)+" stdev(s).")
    plt.axhline(0.5)
    upperExtremeBd = 0.5 + numStdDevsToQualityAsExtreme*math.sqrt(0.25/10)
    lowerExtremeBd = 0.5 - numStdDevsToQualityAsExtreme*math.sqrt(0.25/10)
    #plt.axhline(upperExtremeBd)
    plt.axhline(upperExtremeBd)
    plt.axhline(lowerExtremeBd)
    plt.legend(loc = "best")
 
    
flipSim(10000)
print("Theoretical standard deviation of the distr. flip(100) is:"+str(math.sqrt((0.5*0.5)/100)))


    