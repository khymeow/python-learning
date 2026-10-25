"""
LeetCode 20：有效的括号
难度：Easy

题目：给定仅包含 ()[]{} 的字符串，判断括号是否有效。
每个右括号必须与最近尚未匹配的同类型左括号配对，最终不能剩余左括号。

算法思路：字典加栈
1. 字典记录右括号与对应左括号的关系。
2. 遇到左括号时入栈；遇到右括号时，检查栈是否为空。
3. 栈顶与右括号匹配时出栈，否则返回 False。
4. 遍历结束后，栈为空则返回 True，否则返回 False。

时间复杂度：O(n)
额外空间复杂度：O(n)
"""


class Solution:
    def isValid(self, s):
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in s:
            if i not in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False

        return not stack


def is_valid(s):
    """提供函数入口，调用原始的 Solution.isValid 方法。"""
    return Solution().isValid(s)


if __name__ == "__main__":
    print(is_valid("()"))      # True
    print(is_valid("()[]{}"))  # True
    print(is_valid("(]"))      # False
    print(is_valid("([])"))    # True
    print(is_valid("([)]"))    # False
    print(is_valid("((("))     # False
    print(is_valid("]"))       # False
    print(is_valid("{[]}"))    # True

    # 额外测试：空字符串与多层嵌套括号。
    print(is_valid(""))        # True
    print(is_valid("{[()]}"))  # True
