import sys
'''
Read this Paper
http://oeis.org/A001175

'''
    
def get_piasco_period(m):
    previous = 0
    current = 1 
    for _ in range(m*m):
        previous, current = current, (previous + current)%m
        if previous is 0 and current is 1:
            break
    return _+1

def cal_fib_lastdigit_partialsum(m,n):
   
    
    previous = 0
    current = 1
    sum_ = 0
    for i in range(1,n+1):
        previous, current = current, (previous + current)%10
        if i>=m:
            sum_ = (sum_ + previous)%10
       
    return sum_

if __name__ == '__main__':
    last_digit = 10
    m,n = input().split(' ')
    length_m = get_piasco_period(int(last_digit))
    m = int(m)
    n = int(n)
    n = n%length_m
    m = m%length_m
    print(cal_fib_lastdigit_partialsum(m,n))