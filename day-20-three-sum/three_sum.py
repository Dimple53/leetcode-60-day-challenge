#LeetCode #15: 3Sum
# https://leetcode.com/problems/3sum/description/

def three_sum_brute(nums):
    result = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)

    return [list(triplet) for triplet in result]


# Approach 2: Sorting + Two Pointers
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


def main():
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [-2, 0, 1, 1, 2]
    ]

    for nums in test_cases:
        print("Input:", nums)
        print("Brute Force:", three_sum_brute(nums))
        print("Two Pointers:", three_sum(nums))
        print()


if __name__ == "__main__":
    main()