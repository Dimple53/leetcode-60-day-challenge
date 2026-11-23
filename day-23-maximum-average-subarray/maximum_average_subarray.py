#Leetcode 643. Maximum Average Subarray 
#https://leetcode.com/problems/maximum-average-subarray/

def find_max_average_brute(nums, k):
    max_average = float('-inf')

    for i in range(len(nums) - k + 1):
        window_sum = 0

        for j in range(i, i + k):
            window_sum += nums[j]

        average = window_sum / k
        max_average = max(max_average, average)

    return max_average


# Approach 2: Sliding Window (Optimized)
def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


def main():
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4),
        ([5], 1),
        ([0, 4, 0, 3, 2], 1)
    ]

    for nums, k in test_cases:
        print("Input:", nums)
        print("K:", k)
        print("Brute Force:", find_max_average_brute(nums, k))
        print("Sliding Window:", find_max_average(nums, k))
        print()


if __name__ == "__main__":
    main()