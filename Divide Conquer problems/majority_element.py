'''
Created on Mar 11, 2018

@author: nirmal
'''
# Uses python3
import sys

def find_candidate(a):
    size = len(a)
    maj = 0 
    count = 1
    for idx, val in enumerate(a):
        if a[maj] == a[idx]:
            count = count+1
        else:
            count = count-1
        if count ==0:
            maj =idx
            count =1
    return maj

def get_majority_element(a):
    size = len(a)
    maj = find_candidate(a)
    count = 0
    for idx, val in enumerate(a):
        if a[idx] == a[maj]:
            count = count +1
    if count>size/2:
        return 1
    else:
        return 0

# def get_majority_element(a, left, right):
#     mid = math.floor((left+right)/2)
#     left1, right1 = left, mid
#     left2, right2 = mid, right
#     
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     mid = math.floor((left+right)/2)
#     get_majority_element(a,left,mid)
#     get_majority_element(a,mid,right)
#     #write your code here
#     return -1
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_majority_element(a))