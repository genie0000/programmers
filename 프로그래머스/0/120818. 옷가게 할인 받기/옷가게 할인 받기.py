def solution(price):
    answer = 0
    if 300000 > price >= 100000:
        answer = price - price * 0.05
    elif 500000 > price >= 300000:
        answer = price - price * 0.1
    elif price >= 500000:
        answer = price - price * 0.2
    else:
        answer = price
    return int(answer)