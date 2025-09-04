def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(0, len(A)):
        answer = answer + A[i]*B[i]

    return answer