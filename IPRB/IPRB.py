from __future__ import division
import sys


def pop(k,m,n):
    #s=raw_input()
    #k, m, n = [int(x) for x in s.split(' ')]
    T = k + m + n
    mf = m/T * (1/4 * (m-1)/(T-1) + 1/2 * n/(T-1)) # P(recessive | first parent = Dd)
    nf = n/T * (1/2 * m/(T-1) + (n-1)/(T-1)) # P(recessive | first parent = dd)
    return (1 - mf - nf)


k=raw_input("Enter k\n")
k=int(k)

m=raw_input("Enter m\n")
m=int(m)

n=raw_input("Enter n\n")
n=int(n)


print pop(k,m,n)
