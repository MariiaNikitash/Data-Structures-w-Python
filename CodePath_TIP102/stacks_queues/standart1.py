#  * - * - * - * - Standard Problem Set Version 1 - * - * - * - * - * -
#Problem 1: Valid Parenthesis
# Understand:
#input a string, output a bool
# # Plan iterate over s, if open braket add to a stack
#if closing check if theres something in stack or if its same as open then pop open from stck, otherwise F

#Implement 
def is_valid_post_format(s):
    dic = {'(' : ')', '{' : '}', '[' : ']' }
    stack = []
    for braket in s:
        if braket in dic:
            stack.append(braket)
        else:
            if len(stack) == 0 or braket != dic[stack.pop()]:
                return False
    return not stack


#print(is_valid_post_format("()")) #T
#print(is_valid_post_format("()[]{}")) #T
#print(is_valid_post_format("(]")) #F

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 2: Reverse User Comments Queue
#U: reverse a list in LIFO 
#P: iterate over list, add each comment into stack, then pop to a list ret list
def reverse_comments_queue(comments):
    stack = []
    res = []
    for comment in comments:
        stack.append(comment)
    
    for _ in range(len(stack)):
        res.append(stack.pop())

    return res

#print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
#print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 3: Check Symmetry in Post Titles

def is_symmetrical_title(s):
    s = s.replace(" ", "").lower()
    l,r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True
  

#print(is_symmetrical_title("A Santa at NASA")) #T
#print(is_symmetrical_title("Social Media")) #F

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 4: Engagement Boost
def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
        print(squared_engagement, i)

    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, i in squared_engagements:
        result[position] = square
        position -= 1
    
    return result
#--------------------------
def engagement_b(engagements):
    result = [0] * len(engagements)
    l, r = 0, len(engagements)-1
    last_pos = len(engagements)-1

    while l <= r:
        l_square = engagements[l] * engagements[l]
        r_square = engagements[r] * engagements[r]
        if l_square > r_square:
            result[last_pos] = l_square
            l+=1
        else:
           result[last_pos] = r_square 
           r -=1
        last_pos -=1
  
    return result

#print(engagement_b([-4, -1, 0, 3, 10]))
#print(engagement_b([-7, -3, 2, 3, 11]))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 5: Content Cleaner

#_*------ not working solution !!!!!!!
#def clean_post(post):
#    stack = []
#    res = ""
#    for c in post:
#        if not stack or c != stack[-1]:
#            stack.append(c)
#        else:
#            res +=c
#            stack.pop()
#    while stack:
#        res +=stack.pop()
#    return res, stack


# GOOD SOLUTION # OR I can do c.swapcase()): so if stack and (stack[-1] == char.swapcase()):
def clean_post(post):
    stack = []
    for c in post:
        if stack and abs(ord(c) - ord(stack[-1])) == 32: 
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)
    
print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 6: Post Editor
# ----- Implemented using Deque, but with stack properties (LIFO)

from collections import deque

def edit_post(post):
    stack = deque()
    res = []
    for c in post:
        if c != ' ':
            stack.append(c)
        else:
            while stack:
                res.append(stack.pop())
            res.append(' ')
    
    while stack:
        res.append(stack.pop())

    return ''.join(res)

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog"))



# ----- Implemented using Stack (LIFO)
def edit_post(post):
    stack = []
    res = []
    for c in post:
        if c != ' ':
            stack.append(c)
        else:
            while stack:
                res.append(stack.pop())
            res.append(' ')
    
    while stack:
        res.append(stack.pop())

    return ''.join(res)
print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog"))