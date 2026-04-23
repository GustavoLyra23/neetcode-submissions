class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = [')', ']', '}']
        paris = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if char in closing:
                if not stack or stack[-1] != paris[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0 
