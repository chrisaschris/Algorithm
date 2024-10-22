def solution(s):
    sum_zero=0
    i=0
    while(1):
        if(s=='1'):
            break
        sum=0
        i+=1
        for j in range(len(s)):
            if s[j]=='1':
                sum+=1
            else:
                sum_zero+=1
        s = format(sum, 'b')
        print(s)
    answer = [i, sum_zero]
    return answer