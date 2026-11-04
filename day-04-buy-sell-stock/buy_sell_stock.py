# LeetCode #121: Best Time to Buy and Sell Stock (Easy)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit_brute(prices):
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit


def max_profit_greedy(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit


def max_profit_prefix(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, prices[i])

    return max_profit


# Test cases
test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2], 1),
    ([2, 1], 0),
    ([3, 3, 3], 0),
    ([1], 0),
    ([2, 4, 1], 2),
    ([3, 2, 6, 5, 0, 3], 4),
]

solutions = [
    ("Brute Force", max_profit_brute),
    ("Greedy", max_profit_greedy),
    ("Prefix Minimum", max_profit_prefix),
]

for name, solution in solutions:
    print(f"\n--- {name} ---")

    for prices, expected in test_cases:
        result = solution(prices)
        status = "PASS" if result == expected else "FAIL"

        print(
            f"{status} | Input: {prices} "
            f"| Expected: {expected} | Got: {result}"
        )
