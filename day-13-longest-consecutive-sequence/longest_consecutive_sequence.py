#Leetcode #128 : Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

def longest_consecutive_brute(nums):
    longest = 0

    for num in nums:
        current = num
        length = 1

        while current + 1 in nums:
            current += 1
            length += 1

        longest = max(longest, length)

    return longest


def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:

        # Check if num is the starting point
        if num - 1 not in num_set:
            current = num
            length = 1

            # Count consecutive numbers
            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


def main():
    nums = [100, 4, 200, 1, 3, 2]

    print("Input:", nums)
    print("Brute Force:", longest_consecutive_brute(nums))
    print("Optimized:", longest_consecutive(nums))


if __name__ == "__main__":
    main()