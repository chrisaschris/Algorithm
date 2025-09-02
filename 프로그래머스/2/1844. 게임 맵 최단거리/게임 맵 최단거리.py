from collections import deque

def solution(maps):
    H, W = len(maps), len(maps[0])
    if maps[0][0] == 0 or maps[H-1][W-1] == 0:
        return -1

    q = deque([(0, 0, 1)])  # (i, j, dist) 시작 칸을 1로 세기
    visited = {(0, 0)}
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    while q:
        i, j, d = q.popleft()
        if i == H-1 and j == W-1:
            return d
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and maps[ni][nj] == 1 and (ni, nj) not in visited:
                visited.add((ni, nj))
                q.append((ni, nj, d + 1))
    return -1