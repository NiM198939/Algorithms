'''
Created on Feb 21, 2018

@author: nirmal
'''
def calc_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    fb = [0] * (n+1)
    fb[0] = 0
    fb[1] = 1
    for i in range(2,n+1):
        fb[i] = fb[i-1] + fb[i-2]
    return fb[n]%10

n = int(input())
print(calc_fib(n))