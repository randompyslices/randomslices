#!/usr/bin/env python

from math import factorial
from math import pow
from random import randint
from itertools import count

def probgen(M):
    num = den = 1.0*M
    val = 1.0
    while True:
        val = yield val*(num/den)
        num -= 1

def prob(M,N):
    g = probgen(M)
    p = g.next()
    for i in xrange(0,N-1):
        p = g.send(p) 
    return 1. - p

def trials(M,N,n=100):
    ''' Run n trials creating a sample of N from a population size
        of M.  We could compute the probability directly of getting
        repeats but just for the sake of matching the closed form
        approach let's compute the probablity of sets without repeats
        and do 1 - P
    '''
    no_repeats = 0
    for j in xrange(n):
        s2 = [randint(0,M) for j in xrange(0,N)]
        if len(set(s2)) == N:
            no_repeats += 1
    ''' Compute the probability based on n trials '''
    return 1. - float(no_repeats)/n
    
if __name__ == '__main__':
    
    M = int(raw_input("Enter population size M: "))
    N = int(raw_input("Enter sample size N: "))
    n = int(raw_input("Enter number of trials n: "))

    P = prob(M,N)

    print ("M = {0}, N = {1}, P = {2:3.4f}".format(M,N,P))

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
        print('Error between closed form and function: {}'
                .format(abs(Pc-P)))
    except Exception as e:
        print ("Got exception from closed form calculation: " + str(e))

    print ('Difference between running trials and computed probability = {:3.6f}'.
                format(abs(Pt-P)))


