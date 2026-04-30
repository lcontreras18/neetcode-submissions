class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_map = {
                    ']' : '[',
                    '}' : '{',
                    ')' : '('
                }
        for char in s:
            if char in "({[":
                stack.append(char)
            if char in ")}]":
                if stack and my_map.get(char) == stack[-1]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0