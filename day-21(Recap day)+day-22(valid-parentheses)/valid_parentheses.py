#Leetcode 20. Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/


def valid_parentheses_brute(s):
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")

    return len(s) == 0


# Approach 2: Stack (Optimized)
def valid_parentheses(s):
    stack = []

    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in brackets:
            if not stack or stack[-1] != brackets[char]:
                return False

            stack.pop()

        else:
            stack.append(char)

    return len(stack) == 0


def main():
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([])",
        "([)]",
        "{[]}"
    ]

    for s in test_cases:
        print("Input:", s)
        print("Brute Force:", valid_parentheses_brute(s))
        print("Stack:", valid_parentheses(s))
        print()


if __name__ == "__main__":
    main()