#Leetcode #424 Longest Repeating Character Replacement Problem
#https://leetcode.com/problems/longest-repeating-character-replacement/

# Approach 1: Brute Force
def character_replacement_brute(s, k):
    max_length = 0

    for i in range(len(s)):
        count = {}
        max_freq = 0

        for j in range(i, len(s)):
            char = s[j]
            count[char] = count.get(char, 0) + 1

            max_freq = max(max_freq, count[char])

            window_length = j - i + 1
            replacements = window_length - max_freq

            if replacements <= k:
                max_length = max(max_length, window_length)

    return max_length


# Approach 2: Optimized Sliding Window
def character_replacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1

        max_freq = max(max_freq, count[char])

        window_length = right - left + 1

        while window_length - max_freq > k:
            left_char = s[left]
            count[left_char] -= 1
            left += 1

            window_length = right - left + 1

        max_length = max(max_length, window_length)

    return max_length


def main():
    test_cases = [
        ("ABAB", 2),
        ("AABABBA", 1),
        ("AAAA", 0),
        ("ABCDE", 1),
        ("AAAB", 0),
        ("BAAA", 1)
    ]

    for s, k in test_cases:
        print("Input:", s, "| k:", k)
        print("Brute Force:", character_replacement_brute(s, k))
        print("Sliding Window:", character_replacement(s, k))
        print()


if __name__ == "__main__":
    main()