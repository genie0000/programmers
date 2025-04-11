def solution(n):
    answer = 0
    i = 0
    while i*i <= n:
        if n == i*i:
            answer = (i+1) * (i+1)
            i += 1
        else:
            answer = -1
            i += 1
    return answer