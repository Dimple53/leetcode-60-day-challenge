#Leetcode #238 : Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

def product_except_self_brute(nums):
    answer = []

    for i in range(len(nums)):
        product = 1

        for j in range(len(nums)):
            if i != j:
                product *= nums[j]

        answer.append(product)

    return answer


def product_except_self_prefix_suffix(nums):
    n = len(nums)

    prefix = [1] * n
    suffix = [1] * n
    answer = [1] * n

    # Build prefix products
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Build suffix products
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Combine both
    for i in range(n):
        answer[i] = prefix[i] * suffix[i]

    return answer


def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Optimized prefix pass
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]

    # Optimized suffix pass
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer


def main():
    nums = [1, 2, 3, 4]

    print("Input:", nums)

    print("Brute Force:",
          product_except_self_brute(nums))

    print("Prefix + Suffix:",
          product_except_self_prefix_suffix(nums))

    print("Optimized:",
          product_except_self(nums))


if __name__ == "__main__":
    main()
