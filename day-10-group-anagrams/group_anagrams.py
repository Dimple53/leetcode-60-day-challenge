# LeetCode 49 : Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/


def group_anagrams_brute(strs):
    groups = []
    representatives = []

    for word in strs:
        key = "".join(sorted(word))
        placed = False

        for i in range(len(representatives)):
            if representatives[i] == key:
                groups[i].append(word)
                placed = True
                break

        if not placed:
            representatives.append(key)
            groups.append([word])

    return groups


def group_anagrams(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


def main():
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "bca", "cab", "xyz"],
        ["abb", "bab", "bba", "abc"],
    ]

    for strs in test_cases:
        print(f"Input: {strs}")
        print("Brute Force:", group_anagrams_brute(strs))
        print("Optimized:", group_anagrams(strs))
        print("-" * 40)


if __name__ == "__main__":
    main()