# deque는 양방향 큐 이고, 일반 리스트보다 pop, append가 더 빠르기 때문에 BFS구현에 자주 사용된다.
from collections import deque

def solution(begin, target, words):
    # target 단어가 words안에 없으면 바로 0 반환
    if target not in words:
        return 0
    
    # BFS탐색을 위한 큐에 시작단어와 변환 횟수를 튜플 형태로 넣는다.
    queue = deque([(begin, 0)])
    visited = [False] * len(words)
    
    def one_letter_diff(a,b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        if diff == 1:
            return True
        return False
    
    # 큐에 요소가 있을 동안 계속 반복
    while queue:
        # 큐에서 현재 단어와 변환 횟수를 꺼낸다.
        # popleft()는 큐의 맨 앞에서 꺼내는 함수이다.)
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps
        for i in range(len(words)):
            if not visited[i] and one_letter_diff(current_word, words[i]):
                visited[i] = True
                queue.append((words[i], steps + 1))
    return 0
        
    
    