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
    

    # Solution: add all the opening brakets to the stack then when we encounter
    # a closing braket we have to pop a last opening braket in the stack and compare if closing braket mathces opening braket in the dic
    # if we start of with a closing braket, the stack will be empty so we return false immediately
    # at the end we have to return an empty stack to ensure that no unmatches brakets remain