# LeetCode #283 : Move Zeroes (Easy)
# https://leetcode.com/problems/move-zeroes/


# Approach 1: Brute Force - Repeated Shifting
# Time: O(n²), Space: O(1)

def move_zeroes_brute(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1

# Approach 2: Two Pointers - Write and Fill
# Time: O(n), Space: O(1)

def move_zeroes(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1


# Approach 3: Two Pointers - Swap
# Time: O(n), Space: O(1)

def move_zeroes_swap(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


# Test Cases
if __name__ == "__main__":

    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3],
        [0, 0, 0],
        [1, 0, 0, 2],
        [0, -1, 0, -3],
        [4, 0, 4, 0, 2]
    ]

    for test in test_cases:
        print("Input:", test)

        nums1 = test.copy()
        move_zeroes_brute(nums1)
        print("Brute Force:", nums1)

        nums2 = test.copy()
        move_zeroes(nums2)
        print("Two Pointers (Write + Fill):", nums2)

        nums3 = test.copy()
        move_zeroes_swap(nums3)
        print("Two Pointers (Swap):", nums3)

        print("-" * 45)

 