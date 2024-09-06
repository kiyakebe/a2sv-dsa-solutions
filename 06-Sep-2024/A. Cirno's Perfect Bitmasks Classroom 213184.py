# Problem: A. Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

class BitManipulation:
    def __init__(self):
        pass
    
    def turn_of_kth_bit(self, num, k):
        return  num & ~(1<<k)

    def toggle_kth_bit(self, num, k):
        return num ^ (1 << k)
    
    def set_kth_bit(self, num, k):
        return num | (1 << k)
    
    def is_set(self, num, k):
        return num & (1 << k) != 0
    
    def power_of_two(self, num):
        return num.bit_count() == 1

bm = BitManipulation()

for _ in range(int(input())):
    x = int(input())
    
    if x.bit_count() > 1:
        if x % 2 == 1:
            print(1)
        else:
            for i in range(x.bit_length()):
                if bm.is_set(x, i):
                    print(1<<i)
                    break
    else:
        if x % 2 == 0:
            print(bm.set_kth_bit(x, 0))
        else:
            print(3)
            
        