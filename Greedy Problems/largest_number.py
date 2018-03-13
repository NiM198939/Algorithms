#Uses python3

import sys

def largest_number(a):
    #write your code here
    a = sorted(a, key=lambda a: a)
    len_item = len(a[0])
    counter_left = 0
    counter_right = 0
    while len(a)!=0:
        
    
    res = ""
    for x in a:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
