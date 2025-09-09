def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    return dfs(k, dungeons, visited, 0)

def dfs(cur_fatigue, dungeons, visited, count):
    max_count = count

    for i in range(len(dungeons)):
        need, cost = dungeons[i]
        if not visited[i] and cur_fatigue >= need:
            visited[i] = True
            result = dfs(cur_fatigue - cost, dungeons, visited, count + 1)
            max_count = max(max_count, result)
            visited[i] = False  # 백트래킹

    return max_count