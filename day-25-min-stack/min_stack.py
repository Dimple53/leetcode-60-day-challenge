#Leetcode #155 Min Stack - Two Stack Approach
#https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


def main():
    min_stack = MinStack()

    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    print("Minimum:", min_stack.getMin())  # -3

    min_stack.pop()

    print("Top:", min_stack.top())         # 0
    print("Minimum:", min_stack.getMin())  # -2

    print("\nSecond Test Case:")

    stack2 = MinStack()

    stack2.push(5)
    stack2.push(3)
    stack2.push(7)

    print("Minimum:", stack2.getMin())     # 3

    stack2.pop()

    print("Top:", stack2.top())            # 3
    print("Minimum:", stack2.getMin())     # 3


if __name__ == "__main__":
    main()