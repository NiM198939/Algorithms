# Uses python3
import sys

def optimal_summands(n):
    summands = []
    a = 1
    while n!=0:
        sum = n - a 
        if sum == 0:
           summands.append(a)
           return summands
        if sum > a:
            n = sum
            summands.append(a)
        a = a + 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')