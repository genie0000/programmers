def solution(begin, target, words):
    # min_steps는 최소 단계 수를 추적할 리스트, 초기값은 무한대로 설정
    min_steps = [float('inf')]
    # words 리스트에서 각 단어가 사용됐는지 여부를 저장(중복방지를 위함)
    visited = [False] * len(words)
    
    # 두 단어를 비교해서 한 글자만 다른지 확인하는 함수
    def one_letter_diff(a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        if diff == 1:
            return True
        return False
    
    # 재귀함수 정의, current_word(현재 단어), steps(지금까지 변환한 횟수)
    def dfs(current_word, steps):
        if current_word == target:
            min_steps[0] = min(min_steps[0], steps)
            return
        
        for i in range(len(words)):
            if not visited[i] and one_letter_diff(current_word, words[i]):
                visited[i] = True
                dfs(words[i], steps + 1)
                visited[i] = False
    
    # 시작 단어에서부터 DFS 탐색 시작, 단계 수는 0
    dfs(begin,0)
    
    # min_steps가 여전히 무한대면 0을 그게 아니면 min_steps[0]을 반환한다.
    return 0 if min_steps[0] == float('inf') else min_steps[0]
    
    
    return answer