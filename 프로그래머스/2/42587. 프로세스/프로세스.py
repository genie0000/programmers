from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    count = 0
    
    while queue:
        process = queue.popleft()
        if any(process[0] < other_process[0] for other_process in queue):
            queue.append(process)
        else:
            count += 1
            if process[1] == location:
                return count
