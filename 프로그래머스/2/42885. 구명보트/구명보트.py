def solution(people, limit):
    answer = 0
    i=0
    j=len(people)-1
    asc=sorted(people, reverse=False)
    # print(asc)
    # print(i)
    # print(j)
    while(i<=j):
        if asc[i]+asc[j]<=limit:
            i=i+1
            j=j-1
        else:
            j=j-1
        answer=answer+1
    return answer