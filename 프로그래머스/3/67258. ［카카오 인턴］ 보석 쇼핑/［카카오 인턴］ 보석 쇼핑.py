from collections import defaultdict

def solution(gems):
    # 진열된 보석의 종류 수
    u_gem = len(set(gems)) # 중복을 제거하고 난 보석 종류 수
    gem_value = defaultdict(int) # 보석의 개수를 셀 defaultdict
    
    answer = [0, len(gems)-1] # 답의 초깃값
    left = 0 # 왼쪽 포인터
    min_length = len(gems) # 최소길이 초기화
    
    # 오른쪽 포인터를 한 칸씩 이동하면서 구간을 확장
    for right in range(len(gems)):
        gem = gems[right]
        gem_value[gem] += 1 # 현재 보석을 딕셔너리에 갯수 추가
        
        # 현재 구간에 모든 종류의 보석이 포함되었는지 확인
        while len(gem_value) == u_gem:
            if right - left < min_length:
                min_length = right - left
                answer = [left + 1, right + 1]
            
            # 왼쪽에 있느 보석을 줄이면서 구간을 좁힌다.
            gem_value[gems[left]] -= 1
            # 갯수가 0이되면 딕셔너리에서 삭제
            if gem_value[gems[left]] == 0:
                del gem_value[gems[left]]
            left += 1
        
        
    return answer