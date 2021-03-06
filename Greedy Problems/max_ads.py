'''
Created on Mar 10, 2018

@author: nirmal
'''
#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    for i in range(len(a)):
        res += sorted_a[i] * sorted_b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))