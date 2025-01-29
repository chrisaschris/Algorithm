def solution(numbers, target):
    answer = 0
    num=[0,]
    j = 0
    k = 0
    # num.append(1)
    # print(num)
    for i in range(len(numbers)):
        while j<=k:
            num.append(num[j]+numbers[i])
            num.append(num[j]-numbers[i])
            j=j+1
        k=len(num)-1
        # print(j, k, num, num[j])
        
    for i in range(j, len(num)):
        if target == num[i]:
            answer=answer+1
    # for i in range(len(num)):
    #     print(i, num[i])
    return answer