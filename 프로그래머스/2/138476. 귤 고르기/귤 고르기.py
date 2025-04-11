def solution(k, tangerine):
    b = {}
    for size in tangerine:
        if size in b:
            b[size] += 1
        else:
            b[size] = 1
    
    sorted_counter = sorted(b.values(), reverse = True)
    
    total = 0
    answer = 0
    for c in sorted_counter:
        total += c
        answer += 1
        if total >= k:
            break
    return answer
