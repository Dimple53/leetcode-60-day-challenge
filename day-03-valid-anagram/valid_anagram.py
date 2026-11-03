# LeetCode #242: Valid Anagram (Easy) 
# https://leetcode.com/problems/valid-anagram/


# ---------------------------------
# Solution 1: Brute Force
# ---------------------------------

def is_anagram_brute(s, t):

    if len(s) != len(t):
        return False

    used = [False] * len(t)

    for i in range(len(s)):
        found = False

        for j in range(len(t)):

            if s[i] == t[j] and not used[j]:
                used[j] = True
                found = True
                break

        if not found:
            return False

    return True


# ---------------------------------
# Solution 2: Frequency Dictionary
# ---------------------------------

def is_anagram_dict(s, t):

    if len(s) != len(t):
        return False

    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:

        if char not in counts or counts[char] == 0:
            return False

        counts[char] -= 1

    return True


# ---------------------------------
# Solution 3: Frequency Array
# Only for lowercase a-z
# ---------------------------------

def is_anagram_array(s, t):

    if len(s) != len(t):
        return False

    counts = [0] * 26

    for i in range(len(s)):
        counts[ord(s[i]) - ord('a')] += 1
        counts[ord(t[i]) - ord('a')] -= 1

    for count in counts:
        if count != 0:
            return False

    return True


# ---------------------------------
# Solution 4: Sorting
# ---------------------------------

def is_anagram_sort(s, t):

    return sorted(s) == sorted(t)


# ---------------------------------
# TEST CASES
# ---------------------------------

test_cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("aab", "aba", True),
    ("aab", "abb", False),
    ("listen", "silent", True),
    ("a", "a", True),
    ("a", "b", False),
    ("ab", "a", False),
    ("", "", True),
    ("aabb", "bbaa", True),
    ("abc", "cba", True),
    ("abc", "abd", False)
]


# ---------------------------------
# RUN ALL SOLUTIONS
# ---------------------------------

solutions = [
    ("Brute Force", is_anagram_brute),
    ("Frequency Dictionary", is_anagram_dict),
    ("Frequency Array", is_anagram_array),
    ("Sorting", is_anagram_sort)
]

for name, solution in solutions:

    print("\n", "=" * 45)
    print(name)
    print("=" * 45)

    for s, t, expected in test_cases:

        result = solution(s, t)

        status = "PASS" if result == expected else "FAIL"

        print(
            f"s={s!r}, t={t!r} | "
            f"Expected={expected} | "
            f"Got={result} | {status}"
        )
