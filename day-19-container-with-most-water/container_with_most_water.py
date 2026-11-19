#LeetCode #11: Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

def max_area_brute(height):
    max_area = 0
    n = len(height)

    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            current_height = min(height[i], height[j])

            area = width * current_height

            max_area = max(max_area, area)

    return max_area


# Approach 2: Two Pointers (Optimized)
def max_area(height):
    left = 0
    right = len(height) - 1

    max_area = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])

        area = width * current_height

        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def main():
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [4, 3, 2, 1, 4]
    ]

    for height in test_cases:
        print("Input:", height)
        print("Brute Force:", max_area_brute(height))
        print("Two Pointers:", max_area(height))
        print()


if __name__ == "__main__":
    main()