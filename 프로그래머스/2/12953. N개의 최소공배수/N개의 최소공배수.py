# from collections import Counter

# def isprime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# def solution(arr):
#     answer = 0
#     lst = []
#     anslst = []
#     for num in range(2,101):
#         if isprime(num):
#             lst.append(num)
#     for num in arr :
#         for nn in lst :
#             while(nn<=num):
#                 if num % nn == 0:
#                     anslst.append(nn)
#                     num = num / nn
#                 else :
#                     break
#     counts = Counter(anslst)
#     print(counts)
    
    
#     for x, y in counts :
#         print(x, y)
        
    
#     return answer

# # 2 2,3 2,2,2 2,7


from math import gcd
from functools import reduce

def lcm_pair(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    # abs로 부호 정리, 먼저 나눠 overflow/거대중간값 최소화
    return (abs(a) // gcd(abs(a), abs(b))) * abs(b)

def solution(arr) -> int:
    if not arr:
        return 1  # 관례적으로 공집합의 LCM=1
    return reduce(lcm_pair, arr, 1)