# 힙은 가장 작은 값 또는 가장 큰 값을 빠르게 꺼낼 수 있도록 해주는 자료구조이다.
import heapq

def solution(n, works):
    answer = 0
    i = 0
    
    # heapq는 최솟값을 뽑아주는 힙이기 때문에, 모든 작업량을 음수로 바꾸면 가장 큰 값이 가장 작은 값이 된다.
    works = [-work for work in works]
    # works 리스트를 힙 구조로 변환하는 코드이다.
    heapq.heapify(works)
    
    # 반복 횟수만 필요하고 변수 자체는 안 쓸 때 _를 사용할 수 있다.
    for _ in range(n):
        # 힙에서 꺼낼 값이 0이면 종료
        if works[0] == 0:
            break
        # 힙에서 가장 작은 값을 꺼내 -를 붙여 원래 양수값으로 바꾸고 1을빼서 작업량을 하나씩 줄이고, 줄인 작업량을 다시 힙에 넣는다.(이때 다시 음수로 바꾸어 넣어야 한다.)
        else:
            max_work = -heapq.heappop(works) - 1
            heapq.heappush(works, -max_work)
    
    # works에는 음수 값들이 들어있지만, 제곱을하면 양수값으로 변환된다.
    for work in works:
        answer += work * work

    return answer