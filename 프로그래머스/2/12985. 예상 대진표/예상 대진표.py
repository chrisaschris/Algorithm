def solution(n,a,b):
    answer = 0

    while(1):
        # print(a, b)
        if (a == b+1 and a%2==0) or (a+1 == b and b%2==0):
            answer = answer + 1
            break
        else:
            answer = answer + 1
            if a % 2 == 1:
                a = a+1
            if b % 2 == 1:
                b = b+1
            a = a/2
            b = b/2

    return answer