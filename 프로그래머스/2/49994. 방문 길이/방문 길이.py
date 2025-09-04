def solution(dirs):
    answer = 0
    x, y = 0, 0
    # nx, ny = 0, 0
    visited = set()
    for way in dirs:
        nx, ny = x, y
        # print(visited)
        if way == 'U' and y < 5:
            ny = y+1
        elif way == 'D' and y > -5:
            ny = y-1
        elif way == 'L' and x > -5:
            nx = x-1
        elif way == 'R' and x < 5:
            nx = x+1
        
        if (nx, ny) == (x, y):
            continue
        edge = tuple(sorted(((x, y), (nx, ny))))
        if edge not in visited :
            visited.add(edge)
        
        x, y = nx, ny
    answer = len(visited)
    return answer