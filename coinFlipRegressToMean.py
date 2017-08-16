


import random, math
from statistics import mean, stdev
import pylab as plt

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
    plt.clf()
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
    plt.axhline(upperExtremeBd)
    plt.axhline(lowerExtremeBd)
    plt.legend(loc = "best")
    plt.savefig("regress2Mean"+str(numTrials)+"Trls"+str(numStdDevsToQualityAsExtreme)+"stdevsExtreme.png")
    
illustrateRegressionToMean(50, 1)
illustrateRegressionToMean(200,2)