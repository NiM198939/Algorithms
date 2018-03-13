'''
Created on Feb 22, 2018

@author: nirmal
'''

'''
Use Euclidean GCD to solve this gcd in easy steps
'''
import sys
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gdc_euclidean(a,b):
    while b != 0:
        (a,b) = (b,a%b)
    return a
   

if __name__ == "__main__":
    a,b = input().split(' ')
    print(gdc_euclidean(int(a), int(b)))