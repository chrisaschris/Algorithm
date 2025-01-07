def solution(nums):
    answer = 0
    tmp = []
    for i in nums:
        if(len(tmp)==len(nums)/2):
            break
        if i not in tmp:
            tmp.append(i)
    answer = len(tmp)
    return answer