
import random 
import pylab as plt
import statistics

"""
This script plots confidence intervals for the mean proportion of 
heads over samples of 100 trials of numFlips flips- where numFlips ranges between
2**3 and 2**10, by powers of 2. These confidence intervals are plotted 
against each value of numFlips.

The proportion of heads associated with every numFlips flips is a dataelement and numTrials of them comprise a sample
of size numTrials. The proportion of heads in numFlips flips is treated as a regular numeric variable; a sample of size
numTrials such proportions is taken for each value of numFlips. The means and standard deviations of each sample are computed.
For each value of numFlips, an errorbar centered around the associated sample mean and the extending 1.96 times the associated
standard deviation on either side of the sample mean is drawn. The sample means are connected by a horizontal line.

The statistics here is likely somewhat suspect.
"""


def flipSim(numTrials, flipCounts):
    l=["H", "T"]
    means, sds = [], []
    for numFlips in flipCounts:
        trialVals = []
        for trial in range(numTrials):
            numHeads = 0
            for i in range(numFlips):
                if random.choice(l)=="H":
                    numHeads+=1
            trialVals.append(numHeads/float(numFlips))
        means.append(statistics.mean(trialVals))
        sds.append(statistics.stdev(trialVals))
    plt.errorbar(flipCounts, means, yerr = 1.96*plt.array(sds))
    plt.semilogx()

def doSim():
    ct = [2**i for i in range(3,11)]
    flipSim(100, ct)

doSim()

    
    
