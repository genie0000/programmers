import heapq

def solution(tickets):
    queue = []
    heapq.heappush(queue, (["ICN"], tickets))
    
    while queue:
        route, remain = heapq.heappop(queue)
        
        if not remain:
            return route
    
        # 현재 마지막으로 추가된 공항 위치
        last = route[-1]

        for i, (start, end) in enumerate(remain):
            if start == last:
                new_route = route + [end]
                # i번째 항공권만 제거한 새로운 remain리스트
                new_remain = remain[:i] + remain[i+1:]
                # 새로운 경로와 남은 항공권 리스트를 우선순위 큐에 넣는다.
                heapq.heappush(queue, (new_route, new_remain))
