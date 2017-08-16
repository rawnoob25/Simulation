"""

Explores the relationship between the number of coinflips (nFlips)
and the mean and standard deviation of n(heads)/n(tails) and abs(n(heads) - n(tails))
for samples of 20 trials- each with nFlips coinflips. The mean and standard deviation
of differences and ratios- measured for each nFlip subject- which consists of 
a sample of 20 coinflips- vs the corresponding nFlip number of flips values.

The number of flips ranges between 2**4 and 2**20, by powers of 2.

Four plots are made:
    (1) mean(n(heads)/n(tails)) vs number of flips
    (2) stdev(n(heads)/n(tails)) vs number of flips
    (3) mean(abs(n(heads) - n(tails))) vs number of flips
    (4) stdev(abs(n(heads) - n(tails))) vs number of flips
    =
"""

import random, pylab as plt
import statistics
def makePlot(xVals, yVals, xlab, ylab, title, marker, logX, logY, fileName):
    plt.clf()
    plt.figure()
    plt.plot(xVals, yVals, marker)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    if logX:
        plt.semilogx()
    if logY:
        plt.semilogy()
    plt.savefig(fileName)
    
lst = ["H","T"]
def runTrial(numFlips):
    """
    simulates numFlips coinflips and returns the number
    of heads
    """
    headCt = 0 
    for i in range(numFlips):
        if random.choice(lst)=="H":
            headCt+=1
    return headCt

def flipSim(numTrials):
    flipCts = [2**i for i in range(4,21)]
    meanRatios, stdevRatios, meanDiffs, stdevDiffs = [], [], [], []
    for nFlips in flipCts:
        print("Starting computation for "+str(nFlips)+" flips.")
        ratios, diffs = [], []
        for i in range(numTrials):
            nHeads = runTrial(nFlips)
            nTails = nFlips - nHeads
            diffs.append(abs(nHeads - nTails))
            try:
                ratios.append(nHeads/nTails)
            except ZeroDivisionError:
                continue
        meanRatios.append(statistics.mean(ratios))
        stdevRatios.append(statistics.stdev(ratios))
        meanDiffs.append(statistics.mean(diffs))
        stdevDiffs.append(statistics.stdev(diffs))
    makePlot(flipCts, meanRatios, "Number flips", "mean(n(heads)/n(tails))", "Variability in mean ratio of number\n of heads to number tails\n with the number of coin flips", "bo", True, False, "meanRatioFlip.png")
    makePlot(flipCts, stdevRatios, "Number flips", "stdev(n(heads)/n(tails))", "Variability in stdev of ratio\n of number of heads to number\n of tails with number of coin flips", "bo", True, True, "stdevRatioFlip.png" )
    makePlot(flipCts, meanDiffs, "Number of Flips", "mean(abs(n(heads) - n(tails)))", "Variability in \n(mean (absolute difference between (number of heads and number of tails)))\n with number of coin flips", "bo", True, True, "meanDiffFlip.png")
    makePlot(flipCts, stdevDiffs, "Number of Flips", "stdev(abs(n(heads) - n(tails)))", "Variability in \n(stdev(absolute difference between (number of heads and number of tails)))\n with number of coin flips", "bo", True, True, "stdevDiffFlip.png")
flipSim(20)