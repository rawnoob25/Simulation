"""
Script simulates the number of shots required for 
an 80% freethrow shooter to miss. 1000 trials are simulated- each
consisting of a sequence of freethrow shots the first miss. A histogram
of the number of shots required until the first miss is then plotted.

"""

import random
import pylab as plt

def shootTillMiss(pct):
    ct = 0
    while True:
        ct+=1
        if random.random()>pct:
            return ct
        if ct > 10000:
            print("Took way too many trials")
            return None


def runSim(numTrials, pct):
    cts = []
    for i in range(numTrials):
        trial = shootTillMiss(pct)
        if trial:
            cts.append(trial)
            
    plt.hist(cts, bins = 20)
    plt.xlabel("Number Shots Required to miss")
    plt.title("Histogram of number of shots required ot miss by a(n) "+str(int(100*pct))+" percent freethrow shooter")

runSim(1000, 0.8)