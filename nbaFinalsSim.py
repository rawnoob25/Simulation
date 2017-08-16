"""
The round of the NBA playoffs (including the finals) is comprised 
of 7 games. The team that wins the best of seven games wins the round.

This script explores the the question "What's the minimum win percentage
that one team must have against another in order to win 99% of NBA finals series
against the other team?"

500 such NBA finals series are simulated.
"""
import random
import pylab as plt
import math

def playSeries(winPct, seriesLen):
    won = 0
    for i in range(seriesLen):
        if random.random()<winPct:
            won+=1
    if won>seriesLen//2:
        return 1
    else:
        return 0

def runSim(nTrials):
    winProb = 0.5
    probs = []
    winPercentages = []
    while winProb<=1:
        probs.append(winProb)
        winCt = 0
        for trial in range(nTrials):
            if playSeries(winProb, 7):
                winCt+=1
        winPercentages.append(winCt/float(nTrials))
        winProb+=0.01
    
    plt.plot(probs, winPercentages, 'bo')
    plt.xlabel("Single Game Win Percentage")
    plt.ylabel("Finals Series Win Percentage")
    plt.title("NBA Finals Win Percentage vs\n Single Single Game Win Percentage\nFor Pair of Teams" )
    plt.axhline(0.99)
    
    def findMinSingleGameWinPctFor99PctSeries():
        n = len(winPercentages)
        lo, hi = 0, n-1
        while(lo<=hi):
            mid = (lo+hi)//2
            if winPercentages[mid]>=0.99 and winPercentages[mid-1]<0.99:
                return probs[mid]
            elif winPercentages[mid]<0.99:
                lo = mid+1
            else:
                hi = mid - 1
        raise Exception("Invalid state")
    
    plt.annotate("Lowest Rqd single game win pct for\n 99% series win pct:"+str(round(100*findMinSingleGameWinPctFor99PctSeries(),2)), size='large', xycoords = 'axes fraction', xy= (0.3,0.3))
    #print("The lowest single game win percentage required to win the series 99% of the time is "+str(findMinSingleGameWinPctFor99PctSeries()))
    

runSim(500)
