# LeetCode #217: Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/
#
# Problem: Given an integer array, return True if any value appears at least
#          twice, and False if every element is distinct.
#
# Approach 1: Brute force - compare every pair.
#             Time: O(n^2), Space: O(1)
# Approach 2: Hash set - remember seen numbers, stop at the first repeat.
#             Time: O(n), Space: O(n)
# Approach 3: Sorting - duplicates end up next to each other.
#             Time: O(n log n), Space: O(1) extra if sorted in place
#             (note: nums.sort() changes the input list)
# Approach 4: One-line set trick - compare len(set(nums)) with len(nums).
#             Time: O(n), Space: O(n)


def contains_duplicate_brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  
            if nums[i] == nums[j]:
                return True
    return False  # time limit exceeded for large inputs, so we need a better approach


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:  # have we met this number before?
            return True
        seen.add(num)  # remember it for later
    return False


def contains_duplicate_sort(nums):
    nums.sort()  # sorts the list in place, so the original order is lost
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:  # neighbours are equal
            return True
    return False


def contains_duplicate_oneliner(nums):
    return len(set(nums)) != len(nums)


# Testing: every approach must pass every test
approaches = [
    contains_duplicate_brute,
    contains_duplicate,
    contains_duplicate_sort,
    contains_duplicate_oneliner,
]

tests = [
    ([1, 2, 3, 1], True),  # duplicate at the end
    ([1, 2, 3, 4], False),  # no duplicate
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),  # many duplicates
    ([5], False),  # single element
    ([7, 7, 7], True),  # all the same
    ([-1, 0, -1], True),  # negative numbers
    ([1, 1, 2, 3], True),  # duplicate at the start
]

for func in approaches:
    for nums, expected in tests:
        assert func(list(nums)) == expected, f"{func.__name__} failed on {nums}"
    print(f"{func.__name__}: all tests passed")

print("All approaches passed")