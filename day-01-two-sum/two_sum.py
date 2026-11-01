# LeetCode #1: Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
#
# Problem: Given an array of integers and a target, return the indices
#          of the two numbers that add up to the target.
#          Use two different positions, never the same element twice.
#
# Approach 1: Brute force - check every pair of numbers.
#             Time: O(n^2), Space: O(1)
# Approach 2: Hash map - one pass, look up the complement (target - num).
#             Time: O(n), Space: O(n)
 

def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n): # start at i + 1 so we never reuse an element
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num # the number we need to reach the target
        if complement in seen:           
            return [seen[complement], i]
        seen[num] = i # save AFTER checking, so a number never pairs with itself
    return []  # no pair found


# Testing
print(two_sum_brute([2, 7, 11, 15], 9))  # expected: [0, 1]
assert two_sum_brute([3, 3], 6) == [0, 1]
assert two_sum_brute([3, 2, 4], 6) == [1, 2]
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
print("All tests passed")
