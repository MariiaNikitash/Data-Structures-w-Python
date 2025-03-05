# STRINGS

names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35]
zipped = zip(names, ages)
#print(list(zipped)) # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")
#print(count_mississippi(6))


def swap_ends(my_str):
    if len(my_str) < 2:
        return my_str
    return my_str[-1] + my_str[1:-1] + my_str[0] # last + middle + first    
    return s
my_str = "boat"
swapped = swap_ends(my_str)
#print(swapped) #toab

def is_pangram(my_str):  
    '''Pangram is when each letter in alphabet
       exists in the string at least once'''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in my_str.lower():
            return False
    return True

my_str = "The quick brown fox jumps over the lazy dog"
#print(is_pangram(my_str)) #T
str2 = "The dog jumped"
#print(is_pangram(str2)) #F

def reverse_string(my_str):
    return my_str[::-1]

#OR
def reverse_string(my_str):
    r = ''
    for c in my_str:
        r = c + r
    return r
my_str = "live"
#print(reverse_string(my_str))


def first_unique_char(my_str):
    dic = {}
    for c in my_str:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    
    for i, num in enumerate(my_str):
        if dic[num] == 1:
            return i
    return -1
    
my_str = "leetcode"
#print(first_unique_char(my_str))#0
str2 = "loveleetcode"
#print(first_unique_char(str2)) #2
str3 = "aabb"
#print(first_unique_char(str3)) #-1



def min_distance(words, word1, word2):
    if not word1 or not word2:
        return -1
    pos1 = None
    pos2 = None
    min_dist = float('inf')
    
    for i, str in enumerate(words):
        if str == word1:
            pos1 = i
        if str == word2:
            pos2 = i
    
    if pos1 is not None and pos2 is not None:
            min_dist = min(min_dist, abs(pos1 - pos2))

    return min_dist if min_dist != float('inf') else -1


words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)





