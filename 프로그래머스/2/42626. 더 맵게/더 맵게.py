from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville and scoville[0]<K:
        if len(scoville)==1:
            answer = -1
            break
        heappush(scoville,heappop(scoville)+heappop(scoville)*2)
        answer+=1
    return answer