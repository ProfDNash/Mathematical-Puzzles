"""
SIMULATE THE FAMOUS AIRPLANE SEAT PROBLEM

@author: David A. Nash
@initial date: 9/1/2020
"""
import numpy as np
import matplotlib.pyplot as plt

def calcProp(counter,t):
    ##A function to calculate the running proportion of cases
    if t==0:
        return 0
    else:
        return np.sum(counter[:t])/t

def fillPlane():
    passengers = np.arange(100)
    np.random.shuffle(passengers) ##put the passengers in a random order
    seats = np.zeros((1,100)) ##each passenger number corresponds to their assigned seat
    ##place the first passenger randomly regardless of their assigned seat
    firstSeat = np.random.randint(0,100)
    seats[0,firstSeat] = 1  ##1 means the seat is filled, 0 means it is empty
    for p in range(1,99):
        pickedSeat = passengers[p]
        if seats[0,pickedSeat]==0: ##if assigned seat is empty, take it
            seats[0,pickedSeat]=1
        else:  ##pick a new seat randomly
            while seats[0,pickedSeat]==1:
                pickedSeat = np.random.randint(0,100)
            seats[0,pickedSeat]=1
    ##check to see if the last passenger can sit in their own seat
    if seats[0,passengers[99]]==0:
        #print('Seat available!')
        return 1
    else:
        #print('Seat taken!')
        return 0

def runTrials(n):
    ##keep track of the results over n trials and visualize them
    counter = np.zeros(n)
    countProp = np.zeros(n)
    for r in range(n):
        counter[r] = fillPlane()
        countProp[r] = calcProp(counter,r+1)
    print('Over ' + str(n) + ' trials, the proportion of times the final passenger could sit in their own seat was ', countProp[n-1])
    print('See plot for the running proportion over time.')
    
    fig, ax = plt.subplots()
    ax.plot(np.arange(n),countProp)
    ax.set_ylim(0,1)
    ax.set_yticks([0,0.25,0.5,0.75,1])
    ax.set_title('PROPORTION OF TRIALS IN WHICH THE FINAL SEAT WAS THE CORRECT ONE')
    ax.set_xlabel('Number of Trials')
    ax.set_ylabel('Propoportion')
    plt.show()
        
    
    
    
