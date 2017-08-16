"""
Simulates the K rolls of a fair dice for K in [2,100].
For each value of K, the probability of rolling exactly two
3s is recorded and compared to the actual (theoretical) probability.
The simulated probabilities are plotted vs the associated values of K.
"""

import math, random
import pylab as plt

def nCr(n, r):
    return int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

actVal = lambda k: ((1/6)**2)*((5/6)**(k-2))*nCr(k, 2)


def simKRolls(k):
    hits = 0 
    for i in range(k):
        roll = random.randint(1,6)
        if roll==3:
           hits+=1 
    return hits==2

def computeProb(k, sampleSize):
    ct = 0
    for i in range(sampleSize):
        if simKRolls(k):
            ct+=1
    return ct/float(sampleSize)
    

def runSim():
    probs = []
    sizes = []
    for i in range(2,100):
        probs.append(computeProb(i, 1000))
        sizes.append(i)
    plt.plot(sizes, probs, "bo")
    plt.xlabel("Numbers of rolls")
    plt.ylabel("Probability of rolling exactly two 3s")
    for i in range(2,100):
        print(i, actVal(i))
    
runSim()
    



    
    


