'''
Created on Feb 22, 2018

@author: nirmal
'''
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a, b):
    pa = a
    pb = b
    while b != 0:
        (a,b) = (b,a%b)
    sum_ = int(pa/a)
    return (sum_)*pb

if __name__ == '__main__':
    a,b = input().split(' ')
    print('%d' % (lcm_fast(int(a), int(b))))

