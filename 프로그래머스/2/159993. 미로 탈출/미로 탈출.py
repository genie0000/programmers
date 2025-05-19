import heapq

def a_star(start, goal, maps):
    n, m = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    visited = [[False] * m for _ in range(n)]
    heap = []
    heapq.heappush(heap, (heuristic(start, goal), 0, start))
    
    while heap:
        est_cost, cost, (x,y) = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if (x,y) == goal:
            return cost
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <n and 0 <= ny < m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                new_cost = cost + 1
                est = new_cost + heuristic((nx, ny), goal)
                heapq.heappush(heap, (est, new_cost, (nx, ny)))
    return -1

def solution(maps):
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
    
    to_lever = a_star(start, lever, maps)
    to_exit = a_star(lever, end, maps)
    
    if to_lever == -1 or to_exit == -1:
        return -1
    return to_lever + to_exit

    
                
    
    
    
    return answer