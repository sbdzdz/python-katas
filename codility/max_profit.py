def solution(A):
    if not A:
        return 0
    max_profit = 0
    min_price = max(A)
    for price in A:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max(0, max_profit)
