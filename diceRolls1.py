# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:39:24 2017

Contains function that simulates
10 rolls of fair 6-sided dice and
computes probability of rolling exactly 
2 ones.

A point estimate of the probability 
of rolling exactly 2 ones in a set of 10 rolls
using a sample of size numTrials is computed
by gen_sample_probability(1, 2, 10, numTrials).

gen_95pct_conf_int_for_prop() returns a 95% confidence
interval for such an estimate w/ numTrials as n.

This simulation explores out of 100 such intervals,
how many capture the true proportion. (The true proportion is the proportion of 
sets of 10 rolls among an infinite number of sets of 10 rolls
that result in rolling exactly 2 ones.)
"""
import math, random

def nCr(n, r):
    assert n>=0 and 0<=r<=n
    f = math.factorial
    return int(f(n)/(f(r)*f(n-r)))

def simRoll():
    return random.choice(list(range(1,7)))

def sim_n_rolls(val, k, n):
    """
    Simulates n rolls of fair 6-sided die. Returns
    true if and only if val is rolled exactly k times.
    """
    assert n>0 and 0<=k<=n
    hitCt = 0
    for i in range(n):
        if simRoll() == val:
            hitCt+=1
    return hitCt == k   

def gen_sample_probability(val, k, n, numTrials):
    """
    Simulates numTrials sets of n rolls of a 6-sided fair die.
    Returns a point estimate of the probability of rolling the value, val,
    exactly k times in a set of n rolls.
    
    """
    ct = 0
    for i in range(numTrials):
        if sim_n_rolls(val, k, n):
            ct+=1
    return ct/float(numTrials)
    

def gen_95pct_conf_int_for_prop(prop, n):
    """
    Returns a 95% confidence interval for the proportion
    of times 10 rolls of a 6-sided fair die result in 
    rolling exactly 2 ones.
    """
    sErr = math.sqrt((prop*(1-prop))/n)
    return (prop - 1.96*sErr, prop + 1.96*sErr)

actVal = nCr(10,2)*((1/6)**(2))*((5/6)**8)

def runSim(printOp = True):
    """
    Simulates 10,000 sets of 10 rolls of a 6-sided fair dice.
    Prints a 95% confidence interval for the proportion of sets of 10 rolls
    resulting in exactly two ones being rolled.
    """
    n = 10000
    est = gen_sample_probability(1, 2, 10, n)
    conf_int = gen_95pct_conf_int_for_prop(est, n)
    if printOp:
        print("95% Confidence interval for probability of rolling exactly 2 ones in 10 rolls is:"+str(conf_int))
        print("Actual probability of rolling exactly 2 ones in 10 rolls is: "+str(actVal))
    return conf_int[0]<actVal<conf_int[1]

def numIntervalsThatCaptureTrueProp():
    """
    Returns the proportion of 95% confidence intervals (see above function for details)
    that capture the true proportion when generating 100 intervals. We'd ideally like 
    force this function to return a value >=0.95. However, it may fail to do so
    due to each sample proportion being a poor estimate for the true proportion. The 
    margin of error for each confidence interval is computed using the sample proportion (p_hat)
    as an estimate for p. In this situation- p_hat is the return value of a single call
    to gen_sample_probability.

    """
    ct = 0
    for i in range(100):
        if runSim(False):
            ct+=1
    return ct/float(100)


runSim()
print("Percent of confidence intervals that capture true proportion:"+str(100*numIntervalsThatCaptureTrueProp()))
