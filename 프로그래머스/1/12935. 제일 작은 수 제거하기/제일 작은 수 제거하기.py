def solution(arr):
    answer=arr.copy()
    if len(arr) == 1:
        return [-1]
    arr.sort(reverse=True)
    min=arr.pop()
    print(min)
    answer.remove(min)
    return answer
