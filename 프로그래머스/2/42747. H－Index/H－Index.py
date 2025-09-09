def solution(citations):
    answer = len(citations)
# n 편 중 h 번 이상 인용된 논문이 h 편 이상이고 나머지 논문이 h 편 이하 인용되었다면 h의 최댓값
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i]<i+1:
            answer = i
            break
    
    return answer