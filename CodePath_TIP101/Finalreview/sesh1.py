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


#1. Character Frequency Counter
#Problem:
#Return a dictionary with the count of each character in a string.

def freq(s):
    dic = {}
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] +=1

    return dic
s = "leetcode"
print(freq(s))
#Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


def repeat(s):
    dic = {}
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    for i, c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1

#Input: "leetcode"
#Output: 0 (first 'l' is unique)
print(repeat(s))


