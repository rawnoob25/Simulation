

"""
For i going from 2^4 to 2^20 by powers of 2,
i coinflips are performed, and for each i, the absolute value of the difference between 
number of heads and number of tails is recorded, as is the ratio
of number of heads to the number of tails.

For number(heads):number(tails) ratio vs number of trials, two plots are made: one with both
axes linearly scaled and another with the number of trials(x-axis)
on a log2 scale and the ratio on a linear scale.

For number(heads) - number(tails) vs number of trials, two plots are made: one with
both axes lienarly scaled and another with both axes on a log2 scale

"""


import random
import pylab as plt
def diffsAndRatiosCoinflips(minExp, maxExp):
    numFlips = []
    for i in range(minExp, maxExp+1):
        numFlips.append(2**i)
    diffs, ratios = [], []
    l = ["H", "T"]
    for flipCt in numFlips:
        numHeads = 0
        for i in range(flipCt):
            if random.choice(l)=="H":
                numHeads +=1
        numTails = flipCt - numHeads
        diffs.append(abs(numHeads - numTails))
        try:
            ratios.append(numHeads/numTails)
        except ZeroDivisionError:
            continue
    
    plt.plot(numFlips, ratios,'bo')
    plt.xlabel("Number of coinflips")
    plt.ylabel("number(heads)/number(tails)")
    plt.title("Ratios of number(heads) to number(tails) vs number of coinflips")
    plt.savefig("headsTailsRatios_vs_numFlips_lin.png")
    plt.clf()
    plt.figure()
    plt.plot(numFlips, diffs,'bo')
    plt.xlabel("Number of coinflips")
    plt.ylabel("abs(number(heads) - number(tails))")
    plt.title("Absolute value of difference (number(heads) - number(tails))\n vs number of coinflips")
    plt.savefig("headsTailsAbsDiffs_vs_numFlips_lin.png")
    plt.clf()
    plt.figure()
    plt.plot(numFlips, ratios,'bo')
    plt.semilogx(basex = 2)
    plt.xlabel("log_2(number of coinflips)")
    plt.ylabel("number(heads)/number(tails)")
    plt.title("Ratios of number(heads) to number(tails) \nvs log_2(number of coinflips)")
    plt.savefig("headsTailsRatios_vs_log2(numFlips).png")
    plt.clf()
    plt.figure()
    plt.plot(numFlips, diffs, 'bo')
    plt.semilogx(basex = 2)
    plt.semilogy(basey = 2)
    plt.xlabel("log_2(number of coinflips)")
    plt.ylabel("log_2(abs(number(heads) - number(tails)))")
    plt.title("log2-log2 plot of absolute value of (number(heads) - number(tails))\n vs number of coinflips")
    plt.savefig("log2log2_headsTailsAbsDIffs_vs_numFlips.png")
    
diffsAndRatiosCoinflips(4,20)
    