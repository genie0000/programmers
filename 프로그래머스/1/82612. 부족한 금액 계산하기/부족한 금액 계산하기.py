def solution(price, money, count):
    total_cost = price * (count * (count + 1)) // 2
    shortfall = total_cost - money
    return shortfall if shortfall > 0 else 0
