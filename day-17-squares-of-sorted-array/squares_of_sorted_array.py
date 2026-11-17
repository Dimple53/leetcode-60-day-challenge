#Leetcode # 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

def sorted_squares_brute(nums):
    result = []

    for num in nums:
        result.append(num ** 2)

    result.sort()
    return result

def sorted_squares_sort(nums):
    result = [num ** 2 for num in nums]
    return sorted(result)

def sorted_squares(nums):
    left = 0
    right = len(nums) - 1

    result = [0] * len(nums)
    position = len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1

        position -= 1

    return result


def main():
    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [0, 1, 2, 3, 4]
    ]

    for nums in test_cases:
        print("Input:", nums)
        print("Brute Force:", sorted_squares_brute(nums))
        print("List + Sort:", sorted_squares_sort(nums))
        print("Two Pointers:", sorted_squares(nums))
        print()


if __name__ == "__main__":
    main()