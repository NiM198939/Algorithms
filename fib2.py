import sys
'''
Read this Paper
http://oeis.org/A001175

'''
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def cal_fibno_n_mod_m(n,length_m,m):
    mod = n%length_m
    previous = 0 
    current = 1
    for _ in range(mod):
        previous, current = current, (previous + current)%m
    return previous
    
def get_piasco_period(n,m):
    previous = 0
    current = 1 
    for _ in range(m*m):
        previous, current = current, (previous + current)%m
       
        if previous is 0 and current is 1:
            break
    return _+1

if __name__ == '__main__':
    n,m = input().split(' ')
    length_m = get_piasco_period(int(n), int(m))
    print(cal_fibno_n_mod_m(int(n),length_m,int(m)))