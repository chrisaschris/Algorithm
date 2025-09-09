def solution(clothes):
    answer = 0
    dic = {}
    for x, y in clothes:
        if y in dic:
            dic[y]+=1
        else:
            dic[y]=2
    sums = 1
    for value in dic.values():
        sums*=value
    answer = sums-1
    return answer