# LeetCode Biweekly Contest 195 - Q1: Count Valid Substrings I (Medium)
#https://leetcode.com/contest/biweekly-contest-195/problems/count-valid-substrings-i/


# Brute Force: O(n^3) Time | O(n) Space
# Optimized: O(n) Time | O(1) Space

def count_valid_substrings_brute(s):
    count = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            if "abc" in s[i:j + 1]:
                continue
            count += 1

    return count


def count_valid_substrings(s):
    last_bad_start = -1
    answer = 0

    for right in range(len(s)):
        if right >= 2 and s[right - 2:right + 1] == "abc":
            last_bad_start = right - 2

        answer += right - last_bad_start

    return answer


if __name__ == "__main__":
    test_cases = ["abac", "abc", "a", "abca", "abcabc"]

    for s in test_cases:
        brute_result = count_valid_substrings_brute(s)
        optimized_result = count_valid_substrings(s)

        print(f"Input: {s}")
        print(f"Brute Force: {brute_result}")
        print(f"Optimized:   {optimized_result}")
        print("-" * 30)