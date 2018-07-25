"""
An array A contains daily prices of a stock share for N consecutive days.

Return the maximal profit that can be obtained
by buying a single share on day P and selling it on day Q.

Return 0 if it is impossible to make any money.
"""

def solution(A):
    if not A:
        return 0
    max_profit = 0
    min_price = max(A)
    for price in A:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max(0, max_profit)
