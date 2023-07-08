# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for char in s:
            if not stack:
                stack.append(char)
                continue

            if char in pairs:
                stack.append(char)
                continue

            if stack[-1] not in pairs:
                return False

            if pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False

        return not stack
