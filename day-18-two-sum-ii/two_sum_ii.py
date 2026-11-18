#LeetCode #167 : Two Sum II: Input Array Is Sorted 
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def two_sum_brute(numbers, target):
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

    return []



def two_sum_binary_search(numbers, target):
    n = len(numbers)

    for i in range(n):
        complement = target - numbers[i]

        left = i + 1
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if numbers[mid] == complement:
                return [i + 1, mid + 1]

            elif numbers[mid] < complement:
                left = mid + 1

            else:
                right = mid - 1

    return []

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []


def main():
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1)
    ]

    for numbers, target in test_cases:
        print("Input:", numbers)
        print("Target:", target)

        print("Brute Force:", two_sum_brute(numbers, target))
        print("Binary Search:", two_sum_binary_search(numbers, target))
        print("Two Pointers:", two_sum(numbers, target))
        print()


if __name__ == "__main__":
    main()