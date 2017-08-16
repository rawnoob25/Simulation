import random, pylab as plt

"""
Makes histogram of counts of sum of 3
random integer- each in the range [1,10]
over 10,000 total trials.
"""

def sum3(numTrials):
    tots = []
    for i in range(numTrials):
        v1 = random.randint(1, 10)
        v2 = random.randint(1, 10)
        v3 = random.randint(1, 10)
        tots.append(v1+v2+v3)
    plt.hist(tots, bins = 15)


sum3(10000)   