def solution(array, commands):
    answer = []
    tmp = []
    for i in commands :
        tmp=(array[i[0]-1:i[1]]).copy()
        tmp.sort()
        answer.append(tmp[i[2]-1])
    return answer