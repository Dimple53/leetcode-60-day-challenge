#Leetcode #125 : Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

def valid_palindrome_brute(s):
    cleaned = ""

    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]


# Approach 2: Two Pointers (Optimized)
def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def main():
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " "
    ]

    for s in test_cases:
        print("Input:", repr(s))
        print("Brute Force:", valid_palindrome_brute(s))
        print("Two Pointers:", valid_palindrome(s))
        print()


if __name__ == "__main__":
    main()