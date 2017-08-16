"""
NOTE SIMULATION PRODUCES UNANTICIPATED RESULTS: Neither the function verifyBenfords nor the function verifyBenfords2
produces the expected probability distribution. The distributions generated
by the simulations in both verifyBenfords and verifyBenfords2 have all
digits at similar probabilities.  

In the actual benford distribution, first digit of 1 is the decisive winner at ~30%,
and the decisive runner up is a first digit of 2 at ~18%.

Script runs a simulation to verify Benford's Law.
Roughly speaking, Benford's law states that the 
probability that the first digit of a positive integer, n, 
is d is given by P(d) = log_10(1+ 1/d). 10,000 random
integers between 1 and 10,000 (inclusive of both) are generated.
"""
import random
import pylab as plt
import math

random.seed()

def verifyBenfords(numVals):
    d = {i:0 for i in range(1,10)}
    #l= [] 
    for i in range(numVals):
        val = random.randint(1, 10000)
        while val>=10:
            val//=10
        assert val<10
        d[val]+=1
        #l.append(val)
    probs = {i:d[i]/numVals for i in d.keys()} 
    for i in d.keys():
        print(i, probs[i])
#    plt.hist(l, bins = 9, density = True)

def verifyBenfords2(numVals):
    d = {i:0 for i in range(1,10)}
    for i in range(numVals):
        val = 1 + int(10000*random.random())
        while val>=10:
            val//=10
        assert val<10
        d[val]+=1
    probs = {i:d[i]/numVals for i in d.keys()} 
    for i in d.keys():
        print(i, probs[i])

def printActBenfordVals():
    for d in range(1,10):
        print(d, math.log10(1 + 1/d))

verifyBenfords2(10000)
printActBenfordVals()   


