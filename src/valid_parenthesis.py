class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {"(": ")", "[": "]", "{": "}"}
        open_parentheses = set(parentheses_map.keys())
        stack = []
        for char in s:
            if char in open_parentheses:
                stack.append(char)
            else:
                if not stack or parentheses_map[stack.pop()] != char:
                    return False
        # The stack must be empty or there is a hanging parenthesis
        return not stack
