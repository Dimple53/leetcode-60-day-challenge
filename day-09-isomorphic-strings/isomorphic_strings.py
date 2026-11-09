# LeetCode 205: Isomorphic Strings (Easy)
# https://leetcode.com/problems/isomorphic-strings/description/



def is_isomorphic_brute(s, t):
    mapping = {}

    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                return False
        else:
            if t[i] in mapping.values():
                return False
            mapping[s[i]] = t[i]

    return True


def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
            return False

        if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
            return False

        s_to_t[s[i]] = t[i]
        t_to_s[t[i]] = s[i]

    return True


def main():
    test_cases = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
        ("badc", "baba"),
        ("ab", "aa"),
    ]

    for s, t in test_cases:
        print(f"Input: s={s}, t={t}")
        print("Brute Force:", is_isomorphic_brute(s, t))
        print("Optimized:", is_isomorphic(s, t))
        print("-" * 30)


if __name__ == "__main__":
    main()