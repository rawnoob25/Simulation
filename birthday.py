# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:53:44 2017

Contains code related to the modeling of the
"Birthday Problem". The question answered by the 
Birthday Problem is "What's the probability that
at least K people among a set of N people
have the same birthday (only taking into account the month
and the year")?

The code explores the question both under the scenario
that birthdays are distributed uniformly as well as under the scenario
that birthdays between June 1st and August 31st are 4 times 
as likely as the others.

If K=2, and the distribution of birthdays is uniform, the
question has a convenient (albeit computationally expensive)
closed form solution of P(N) = 366!/(366^N*((366-N)!)).
However, if K=3 (or more), obtaining an analytical solution
to the problem is anywhere from extremely difficult to impossible -
even provided that birthdays are distributed uniformly. It's also anywhere 
from extraordinarily difficult to impossible if the distribution is not uniform 
(even for K=2). It is in these situations that a simulation based method affords 
a distinct advantage.
"""

import random
import math

def birthday_summerBdays_4TimesAsLikely(N, K): 
    
    MONTHS = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30
              , 10:31, 11:30, 12:31}
    totDays = sum(MONTHS[x] for x in MONTHS.keys())
    
    def computeSummerBounds():
        """
        Returns a tuple of form (start:int, end:int) wherein
        start is the day number of the start of summer and end
        is the day number of the start of fall (1 day beyond the end of summer).
        
        Assumes the first day of the year is designated a day number
        of zero.
        
        Assumes that summer begins on June 1st and ends on August 31st.
        """
        start = sum(MONTHS[x] for x in range(1,6))
        end = start + sum(MONTHS[x] for x in range(6,9))
        return (start,end)
    
    summerBds = computeSummerBounds()
    possibleDayNumsList = list(range(0, summerBds[0])) +\
    4*list(range(summerBds[0], summerBds[1])) + list(range(summerBds[1], totDays))
    bdayCtsList = [0 for i in range(366)]
    random.seed()
    for i in range(N):
        dayNum = random.choice(possibleDayNumsList)
        (bdayCtsList[dayNum])+=1
    
    return max(bdayCtsList)>=K
 
    
def compare_birthdays(K, rds):
    """
    For n=10 to 100, by 10, compares the averaged estimated probability (averaged
    over rds rounds) of at least K birthdays being the same under the following 2
    birthday likelihood distributions:
        1) any birthday is as likely as any other
        2) Summer (defined as June 1st to August 31st) birthdays
        are 4 times as likely as the others
        
    Returns a generator that yields, for each value of n, information regarding a comparison
    between the 2 birthday distribution scenarios of the probability of at least K birthdays 
    being the same 
    """
    numBirthdaysList = list(range(10,101,10))
    for n in numBirthdaysList:
        uniformTot, summerWeightedTot = 0, 0
        for rd in range(rds):
            uniformTot += birthdayProb(n, K, 1000)
            summerWeightedTot += birthdayProb(n, K, 1000, "summer_weighted")
        info = "Averaged estimated probabilities of "+str(K)+" birthdays being the same"+\
        " among "+str(n)+" people under 2 distributions are:\n"+"uniform:"+str(uniformTot/rds)+" summer weighted:"+str(summerWeightedTot/rds)+"\n"
        yield info

def birthday(N, K):
    """
    Generates N random birthdays (assuming each birthday is equally likely)
    and returns true if and only if there is at least one date of birth (excluding the year)
    that has at least K occurences
    """
    random.seed()
    numBdaysOnDate = [0 for x in range(366)]
    for i in range(N):
        idx = random.randrange(366)
        (numBdaysOnDate[idx])+=1
    
    return max(numBdaysOnDate)>=K




def birthdayProb(N, K, trials, distr="uniform"):
    """
    Generates N random birthdays (each birthday is equally likely) trials times;
    returns the share of trials for which at least K birthdays were the same. This
    is an estimate of the probability of at least K birthdays being the same
    among a list of N random birthdays.
    """
    
    ct = 0
    for i in range(trials):
        if distr=="uniform":
            if birthday(N, K):
                ct+=1
        elif distr=="summer_weighted":
            if birthday_summerBdays_4TimesAsLikely(N, K):
                ct+=1
        else:
            raise ValueError("Currently, the only allowable values of the \"distr\""+\
                             " parameter are \"uniform\" and \"summer_weighted\"." )
    return ct/trials

    


def runBirthdaySim(K, rds):
    """
    for n in [10, 20, 50, 100, 200], runs through rds simulations of
    performing 1000 trials of generating n random birthdays and checking
    if at least K are the same.
    
    Returns a generator. This generator yields (for each n in [10, 20, 50, 
    100, 200]) a string w/ an averaged estimate (averaged across the rds simulations)
    of the probability of at least K birthdays being the same among a list of
    n birthdays (wherein each birthday is equally likely). If K=2,
    the actual probability is appended to each string supplied
    by the generator.
    """
    
    numBdaysList=[10, 20, 40, 50, 100, 200]
    for n in numBdaysList:
        tot = 0
        for m in range(rds):
            tot+=birthdayProb(n, K, 1000)
        info = "Estimated probabiliy of at least "+str(K)+" birthdays being the same among "\
              +" a list of "+str(n)+" birthdays is:"+str(tot/rds)+"."
        if(K==2):      
              actual = 1 - math.factorial(366)/((366**n)*(math.factorial(366-n)))
              info+=" Actual probability is "+str(actual)+"."
        yield info
        
        
def runUniformSimulations():        
    simGen = runBirthdaySim(2, 10)
    for sim in simGen:
        print(sim)
        print("\n")
    print("Now running simulation to see the probability\
          that at least 3 people among a group of n\
           people for n in [10, 20, 40, 100] have the same birthday"
          )
    
    simGen = runBirthdaySim(3, 10)
    for sim in simGen:
        print(sim)
        print("\n")

def runCompareAtLeast2Same():
    simGen = compare_birthdays(2, 10)
    for val in simGen:
        print(val)
if __name__=="__main__":
    runCompareAtLeast2Same();