def solution(topping):
    n = len(topping)
    pre = [0]*n
    suf = [0]*n

    seen = set()
    for i in range(n):
        seen.add(topping[i])
        pre[i] = len(seen)
    seen.clear()
    for i in range(n-1, -1, -1):
        seen.add(topping[i])
        suf[i] = len(seen)
    answer = 0
    for i in range(n-1): 
        if pre[i] == suf[i+1]:
            answer += 1
    return answer