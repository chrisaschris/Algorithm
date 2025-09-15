# def findmax(land, total, idx, height, maxx):
#     if height == len(land):
#         return total
#     for i in range(len(land[0])):
#         if i != idx:
#             total = total + land[height][i]
#             # print("total",total, "i", i, "height", height, "maxx", maxx)
#             # if(height == len(land)):
#             maxx = max(findmax(land, total, i, height+1, maxx), maxx)
#             # else : 
#             #     findmax(land, total, i, height, maxx)\
#             total -= land[height][i]
#     return maxx

# def solution(land):
#     answer = 0
#     answer = findmax(land, 0, -1, 0, 0)

#     return answer

def solution(land):
    n = len(land)
    # land[0]을 그대로 시작점으로 사용 (4열)
    for i in range(1, n):
        for j in range(4):
            # i행 j열을 밟을 때 가능한 최대값 = 이전 행에서 j열을 제외한 최댓값 + 현재 값
            land[i][j] += max(land[i - 1][k] for k in range(4) if k != j)

    # 마지막 행에서 가장 큰 값이 정답
    return max(land[-1])