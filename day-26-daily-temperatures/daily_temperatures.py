#Leetcode #739 Daily Temperatures Problem
#https://leetcode.com/problems/daily-temperatures/

# Approach 1: Brute Force
def daily_temperatures_brute(temperatures):
    n = len(temperatures)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break

    return answer


# Approach 2: Optimized Monotonic Stack
def daily_temperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index

        stack.append(i)

    return answer


def main():
    test_cases = [
        [73, 74, 75, 71, 69, 72, 76, 73],
        [30, 40, 50, 60],
        [30, 60, 90],
        [90, 80, 70, 60],
        [70, 70, 71]
    ]

    for temperatures in test_cases:
        print("Input:", temperatures)
        print("Brute Force:", daily_temperatures_brute(temperatures))
        print("Monotonic Stack:", daily_temperatures(temperatures))
        print()


if __name__ == "__main__":
    main()