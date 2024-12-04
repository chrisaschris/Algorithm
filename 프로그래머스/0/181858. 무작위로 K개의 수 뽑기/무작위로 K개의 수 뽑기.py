def solution(arr, k):
    answer = []
    i=0
    for num in arr:
        if num not in answer:
            answer.append(num)
            i+=1
        if i==k:
            break
    while(i<k):
        answer.append(-1)
        i+=1
    return answer