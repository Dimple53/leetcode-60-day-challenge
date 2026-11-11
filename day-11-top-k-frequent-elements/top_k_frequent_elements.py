# LeetCode #347 : Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/description/

def top_k_frequent_repeated_max(nums, k):

    freq = {}

    for num in nums:

        freq[num] = freq.get(num, 0) + 1

    result = []

    for _ in range(k):

        most_frequent = max(freq, key=freq.get)

        result.append(most_frequent)

        del freq[most_frequent]

    return result


def top_k_frequent_sorting(nums, k):

    freq = {}

    for num in nums:

        freq[num] = freq.get(num, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return [num for num, count in sorted_freq[:k]]


def main():

    test_cases = [

        ([1, 1, 1, 2, 2, 3], 2),

        ([1], 1),

        ([4, 4, 4, 5, 5, 6, 6, 6, 6, 7], 2),

        ([1, 2, 2, 3, 3, 3], 2),

    ]

    for nums, k in test_cases:

        print('Input:', nums, 'k =', k)

        print('Repeated max:', top_k_frequent_repeated_max(nums, k))

        print('Sorting:', top_k_frequent_sorting(nums, k))

        print()


if __name__ == '__main__':

    main()