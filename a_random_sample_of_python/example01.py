#!/usr/bin/env python

from math import factorial
from math import pow

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

if __name__ == '__main__':
    
    M = int(raw_input("Enter M: "))
    N = int(raw_input("Enter N: "))

    P = prob(M,N)

    print ("M = {0}, N = {1}, P = {2:3.4f}".format(M,N,P))

    ''' Test if equal to closed-form but might get arithmetic
        overflow so try but catch exceptions
    '''

    try:
        Pn = factorial(M)/(factorial(M-N)*pow(M,N))
        Pc = 1. - Pn
        print('Probability computed with closed form = {}'.format(Pc))
        print('Error between closed form and function: {}'.format(abs(Pc-P)))
    except Exception as e:
        print ("Got exception from closed form calculation: " + str(e))


