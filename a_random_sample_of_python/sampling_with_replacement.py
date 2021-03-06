#!/usr/bin/env python

from math import factorial
from math import pow
from random import randint

def prob(M,N):
    M = float(M)
    p = 1.0
    for i in xrange(0,N):
       p = p * (M - i)/M
    return 1.0 - p 

def trials(M,N,n=100):
    ''' Run n trials creating a sample of N from a population size
        of M.  Count the number of outcomes with repeats.  When all
        trials have been run divide the count by the number of 
        trials to get the probability of samples with repeats.
    '''
    repeats = 0
    for j in xrange(n):
        s = [randint(0,M) for j in xrange(0,N)]
        if len(set(s)) != N:
            repeats += 1
    return float(repeats)/n
    
if __name__ == '__main__':
    
    M = int(raw_input("Enter population size M: "))
    N = int(raw_input("Enter sample size N: "))
    n = int(raw_input("Enter number of trials n: "))

    P = prob(M,N)

    print ("M = {0}, N = {1}, n = {2}, P = {3:3.4f}".format(M,N,n,P))

    ''' Try computing purely by running trials '''
    Pt = trials(M,N,n)

    print ("Probability computed experimentally = {:3.4f}".format(Pt))

    ''' Test if equal to closed-form but might get arithmetic
        overflow so try but catch exceptions
    '''

    try:
        Pn = factorial(M)/(factorial(M-N)*pow(M,N))
        Pc = 1. - Pn
        print('Probability computed with closed form = {}'.format(Pc))
        print('Difference between closed form and iterative: {:3.6f}'
                .format(abs(Pc-P)))
    except Exception as e:
        print ("Got exception from closed form calculation: " + str(e))

    print ('Difference between running trials and computed probability = {:3.6f}'.
                format(abs(Pt-P)))


