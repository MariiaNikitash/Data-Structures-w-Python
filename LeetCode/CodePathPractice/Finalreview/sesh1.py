# Review and prep 
# Valid Parenthesis
def valid(s):
    dic = { '(' : ')' , '{' : '}' ,  '[' : ']'}
    stack = []
    for braket in s:
        if braket in dic:
            stack.append(braket)
        elif braket in dic.values():
            if not stack or dic[stack[-1]] != braket: # “What closing bracket do I expect for the top opening bracket?”
                return False
            stack.pop()
    return not stack

s = '(())'
print(valid(s))
# Time: o(n)
# Space: o(n)


