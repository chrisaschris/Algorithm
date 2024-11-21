def solution(arr):
    answer = []
    min_num=min(arr)
    answer = arr
    answer.remove(min_num)
    if(len(answer)==0):
        answer.append(-1)
    return answer