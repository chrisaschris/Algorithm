# def solution(n, left, right):
#     answer = []
#     nn=[[0]*n for i in range(0,n)]
#     for i in range(0, n):
#         for j in range(0, n):
#             if i>j:
#                 nn[i][j]=i+1
#             else:
#                 nn[i][j]=j+1
#     result=[]
#     for i in range(0, n):
#         result=result+nn[i]
#     answer = result[left:right+1]
#     return answer

def solution(n, left, right):
    return [max(k // n, k % n) + 1 for k in range(left, right + 1)]