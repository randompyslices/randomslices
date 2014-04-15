#!/usr/bin/env python

from random import randint
import numpy as np
from timeit import timeit

def sample_without_repeats(M,N):
    while True:
        s = [randint(0,M) for i in xrange(0,2*N)][:N]
        if len(set(s)) == N:
            return s

def sample_no_repeats(M,N):
    while True:
        s = np.random.randint(0,M,N)
        if len(set(s)) == N:
            return s

print 'randint: ', timeit('sample_without_repeats(1000,100)', 
        setup = 'from __main__ import sample_without_repeats',number=100)

print 'NumPy: ', timeit('sample_no_repeats(1000,100)', 
        setup='from __main__ import sample_no_repeats',number=100)

print 'random.sample: ', timeit('random.sample(xrange(0,1000),100)',
        setup='import random',number=100)


