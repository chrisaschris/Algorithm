def solution(n):
    answer = 1
    tmp = [0,1]
    for i in range(2,n+1):
        answer = (tmp[i-1]%1234567+tmp[i-2]%1234567)%1234567
        tmp.append(answer)
    return answer