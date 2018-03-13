'''
Created on Mar 9, 2018

@author: nirmal
'''
'''Pseudocode
    1) Choosing maximum denomination first which is less than the given value is safe choice
      and minimum Q that gets divided by m
    n = 0 
    Loop n <=m
        Choose denomination where 
'''
# Uses python3
import sys

def get_change(m):
    #write your code here
    minimum_coins = 0
    while m!=0:
        q1 = divmod(m, 10);
        q2 = divmod(m, 5);
        q3 = divmod(m, 1);
        item1 = q1[0]
        item2 = q2[0]
        item3 = q3[0]
        
        if item1 == 0 :
            item1 = 9999
        if item2 == 0 :
            item2 = 9999
        if item3 == 0 :
            item3 = 9999
       
        maximum_no_denomination = min(item1,item2,item3)
        minimum_coins = minimum_coins + maximum_no_denomination
        maximum = 0
        if maximum_no_denomination == q1[0]:
           maximum = 10
        elif maximum_no_denomination == q2[0]:
             maximum = 5
        else:
             maximum = 1
        m = m % maximum
    return minimum_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))