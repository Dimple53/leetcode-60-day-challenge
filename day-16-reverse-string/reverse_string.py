#Leetcode 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/

def reverse_string_slicing(s):
    return s[::-1]

def reverse_string_loop(s):
    result = []

    for char in s:
        result.insert(0, char)

    return result

def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return s


def main():
    test_cases = [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"],
        ["a"]
    ]

    for test in test_cases:
        print("Original:", test)

        print("Slicing:", reverse_string_slicing(test))
        print("Loop:", reverse_string_loop(test))

        optimized_input = test.copy()
        print("Two Pointers:", reverse_string(optimized_input))
        print()


if __name__ == "__main__":
    main()