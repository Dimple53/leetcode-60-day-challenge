# LeetCode #383 : Ransom Note (Easy)
#https://leetcode.com/problems/ransom-note

from collections import Counter


def can_construct_brute(ransomNote, magazine):

    available = list(magazine)

    for char in ransomNote:

        if char not in available:

            return False

        available.remove(char)

    return True


def can_construct(ransomNote, magazine):

    counts = Counter(magazine)

    for char in ransomNote:

        if counts[char] == 0:

            return False

        counts[char] -= 1

    return True


def main():

    test_cases = [

        ("a", "b"),

        ("aa", "ab"),

        ("aa", "aab"),

        ("abc", "cbad"),

        ("aab", "ab"),

        ("", "abc"),

    ]


    for ransomNote, magazine in test_cases:

        brute = can_construct_brute(ransomNote, magazine)

        optimized = can_construct(ransomNote, magazine)

        print(f"ransomNote={ransomNote!r}, magazine={magazine!r}")

        print(f"Brute Force: {brute} | Optimized: {optimized}")

        print("-" * 40)


if __name__ == "__main__":

    main()


