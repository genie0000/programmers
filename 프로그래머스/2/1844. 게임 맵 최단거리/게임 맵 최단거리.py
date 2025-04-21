from collections import deque

def solution(maps):
    n = len(maps) # 행 개수
    m = len(maps[0]) # 열 개수
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 위, 아래, 왼쪽, 오른쪽
    queue = deque([(0, 0, 1)]) # 0,0은 시작위치, 1은 첫칸부터 시작하므로 거리 1로 설정
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True # 0,0은 방문했으니 True로 설정
    
    while queue: # 큐에 남은 좌표가 있을 때까지 반복.
        x, y, dist = queue.popleft()
        if x == n - 1 and y == m - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
                
    return -1
                