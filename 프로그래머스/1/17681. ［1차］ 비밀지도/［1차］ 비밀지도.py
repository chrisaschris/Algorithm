def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp=bin(arr1[i]|arr2[i])[2:].rjust(n,'0')
        tmp=tmp.replace('0', ' ').replace('1','#')
        answer.append(tmp)
    return answer