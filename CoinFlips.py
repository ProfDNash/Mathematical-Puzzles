"""
SIMULATE THE COIN-FLIPPING RECORD KEEPING PROBLEM
Over the course of n coin flips, we record the flips immediately following
any flip that is heads.  This simulation is meant to estimate the expected
proportion of heads among the flips that were recorded.

@author: David A. Nash
@initial date: 9/16/2020
"""
import numpy as np
import matplotlib.pyplot as plt

def calcProp(counter,t):
    ##A function to calculate the running proportion of cases
    if t==0:
        return 0
    else:
        return np.sum(counter[:t])/t

def oneTrial(n):
    '''Flip a coin n times and after each flip that is heads (1)
    record the following flip.  Return the proportion of recorded
    flips that are heads'''
    papers = np.array([])
    previousFlip=0
    for i in range(n):
        flip = np.random.randint(0,2)
        if previousFlip==1: ##if the previous flip was heads
            papers = np.append(papers,flip) ##record this flip
        previousFlip=flip
    if len(papers)==0:
        return -1
    else:
        return len(papers[papers==1])/len(papers)

def runTrials(numTrials,trialSize,plotFlag=True):
    '''keep track of the results over numTrials trials,
    each of size trialSize, and visualize the running proportion'''
    counter = np.zeros(numTrials)
    countProp = np.zeros(numTrials)
    for r in range(numTrials):
        trial = oneTrial(trialSize)
        while trial<0: ##ignore trials with no papers
            trial = oneTrial(trialSize)
        counter[r] = trial
        countProp[r] = calcProp(counter,r+1)
    print('Over ' + str(numTrials) + 
          ' trials of size ' + str(trialSize) +
          ', the average proportion of recorded heads is ',
          np.round(countProp[numTrials-1],4))
    if plotFlag:
        print('See plot for the running proportion over time.')
    
        fig, ax = plt.subplots()
        ax.plot(np.arange(numTrials),countProp)
        ax.set_ylim(0,1)
        ax.set_yticks([0,0.25,0.5,0.75,1])
        ax.set_title('PROPORTION OF RECORDED HEADS')
        ax.set_xlabel('Number of Trials')
        ax.set_ylabel('Propoportion')
        plt.show()
    
    return counter 


def compareSizes(maxSize):
    expProps = np.array([])
    numFlips = np.arange(2,maxSize+1)
    for n in range(2,maxSize+1):
        expProps = np.append(expProps,np.mean(runTrials(100000,n,False)))
    print(np.concatenate((numFlips.reshape((len(numFlips),1)), 
                          np.round(expProps,2).reshape((len(expProps),1))), axis=1))
    
    fig, ax = plt.subplots()
    ax.plot(numFlips,expProps)
    ax.set_ylim(0,1)
    ax.set_yticks([0,0.25,0.5,0.75,1])
    ax.set_title('EXPECTED PROPORTION OF RECORDED HEADS')
    ax.set_xlabel('Number of Flips per Trial')
    ax.set_ylabel('Expected Propoportion')
    plt.show()
    
    return expProps
