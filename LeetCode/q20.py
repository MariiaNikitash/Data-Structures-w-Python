class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for key in s:
            if key in pairs:
                stack.append(key)
            elif len(stack) == 0 or key != pairs[stack.pop()]:
                return False
        return len(stack) == 0
    

    