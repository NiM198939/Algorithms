# Uses python3
import sys
class loot:
    def __init__(self, weight,value):
        self.weight = weight
        self.value = value
        self.value_weight = value/weight
    def __repr__(self):
        return repr((self.weight,self.value,self.value_weight))
        
def get_optimal_value(sorted_loot_list,n,w):
    total_value = 0
    for i in range(n):
        if w == 0:
            return round(total_value,4)
        a = min(sorted_loot_list[i].weight, w)
        total_value = total_value + a*sorted_loot_list[i].value_weight
        w = w - a
    return round(total_value,4)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    n = int(n)
    loot_list = []
    capacity = int(capacity)
    for i in range(n):
        l = loot(int(weights[i]),int(values[i]))
        loot_list.append(l)
    sorted_loot_list = sorted(loot_list, key=lambda loot: loot.value_weight, reverse=True)
    opt_value = get_optimal_value(sorted_loot_list,n,capacity)
    print("{:.4f}".format(opt_value))    
   
# if __name__ == '__main__':
#     n,w = input().split(' ')
#     n = int(n)
#     w = int(w)
#     loot_list = []
#     for i in range(n):
#         item_v,item_w = input().split(' ')
#         l = loot(int(item_w),int(item_v))
#         loot_list.append(l)
#     sorted_loot_list = sorted(loot_list, key=lambda loot: loot.value_weight, reverse=True)    
#     print("{:.4f}".format(round(get_optimal_value(sorted_loot_list,n,w),4)))
#     