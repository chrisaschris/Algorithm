def solution(k, dungeons):
    n = len(dungeons)
    visited = [False]*n
    best = 0

    def dfs(cur, cnt):
        nonlocal best
        best = max(best, cnt)

        # 가지치기(남은 걸 전부 가도 갱신 못하면 중단)
        if cnt + (n - sum(visited)) <= best:
            return

        for i, (need, cost) in enumerate(dungeons):
            if not visited[i] and cur >= need:
                visited[i] = True
                dfs(cur - cost, cnt + 1)
                visited[i] = False

    dfs(k, 0)
    return best