# LeetCode # 169 : Majority Element
# https://leetcode.com/problems/majority-element


# Approach 1: Brute Force - O(n²) Time, O(1) Space
def majority_element_brute(nums):
    n = len(nums)

    for candidate in nums:
        count = 0

        for value in nums:
            if value == candidate:
                count += 1

        if count > n // 2:
            return candidate


# Approach 2: Frequency Dictionary - O(n) Time, O(n) Space
def majority_element_hash(nums):
    counts = {}
    threshold = len(nums) // 2

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

        if counts[num] > threshold:
            return num


# Approach 3: Sorting - O(n log n) Time
def majority_element_sort(nums):
    nums.sort()
    return nums[len(nums) // 2]


# Approach 4: Boyer-Moore Voting Algorithm
# O(n) Time, O(1) Space
def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# Test Cases
if __name__ == "__main__":
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
        [1],
        [5, 5, 5, 2, 2]
    ]

    for nums in test_cases:
        print("Input:", nums)
        print("Brute Force:", majority_element_brute(nums))
        print("Hash Map:", majority_element_hash(nums))
        print("Sorting:", majority_element_sort(nums))
        print("Boyer-Moore:", majority_element(nums))
        print("-" * 40)