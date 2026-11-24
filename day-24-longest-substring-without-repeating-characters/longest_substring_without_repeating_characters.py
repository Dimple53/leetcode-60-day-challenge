#Leetcode 3: Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Approach 1: Brute Force
def length_of_longest_substring_brute(s):
    max_length = 0

    for i in range(len(s)):
        char_set = set()

        for j in range(i, len(s)):
            if s[j] in char_set:
                break

            char_set.add(s[j])
            max_length = max(max_length, j - i + 1)

    return max_length


# Approach 2: Optimized Sliding Window
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


def main():
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        " ",
        "",
        "au"
    ]

    for s in test_cases:
        print("Input:", repr(s))
        print("Brute Force:", length_of_longest_substring_brute(s))
        print("Sliding Window:", length_of_longest_substring(s))
        print()


if __name__ == "__main__":
    main()