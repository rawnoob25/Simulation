"""
This script plots an annotated histogram of the counts of percentages of 10 and percentages of 30 freethrows made for a 70% freethrow 
shooter across a sample of 10,000 sets of 10 freethrows 
"""

import random, pylab as plt
import statistics
random.seed()
def genPropMade(shots):
    made = 0
    for i in range(shots):
        if random.random()<0.7:
            made+=1
    return made/float(shots)

def makePlot(l, nBins, title, xlab, ylab, mean, std, n):
    plt.figure(n)
    plt.clf()
    plt.hist(l, nBins)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.annotate("Mean="+str(round(mean,4))+"\nStdev="+str(round(std,4)), size='x-large', xycoords='axes fraction', xy = (0.18, 0.7) )
    
def runSim(nSets):
    vals10, vals40 = [], []
    for i in range(nSets):
        vals10.append(genPropMade(10))
        vals40.append(genPropMade(40))
    makePlot(vals10, 10, "Histogram of Pct of freethrows made among samples of 10 shots", xlab='Percentage', ylab='Count', mean = statistics.mean(vals10), std = statistics.stdev(vals10), n=1)
    makePlot(vals40, 10, "Histogram of Pct of freethrows made among samples of 40 shots", xlab='Percentage', ylab='Count', mean = statistics.mean(vals40), std = statistics.stdev(vals40), n=2)
    
runSim(10000)