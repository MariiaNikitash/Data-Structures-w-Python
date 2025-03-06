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
#print(dist1)
#print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
#print(dist3)


def match_made(dictionary):
	for key, value in dictionary.items():
		print( f"{key} and {value} are a perfect match.") # f-string - string interpolation
        
dic = {'Peanut' : 'Jelly',
       'Spongebob': 'Patrick'}
#print(match_made(dic))

def remove_char(s, n):
#return a string w nth char removed
    return s[:n] + s[n+1:] 
s = "typpo"
fixed_s = remove_char(s, 2)
#print(fixed_s) #typo


def vowel_count(s):
    vowels = "aeoyui"
    count = 0
    for c in s.lower():
        if c in vowels:
            count += 1
    return count
my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
#print(count1)
count2 = vowel_count(my_str2)
#print(count2)
count3 = vowel_count(my_str3)
#print(count3)


def reverse_sentence(sentence):
    words = sentence.split(' ') # ['I', 'solemnly', 'swear', 'I', 'am', 'up', 'to', 'no', 'good']
    reversed_list = words[::-1] # ['good', 'no', 'to', 'up', 'am', 'I', 'swear', 'solemnly', 'I']
    rev_sent = ' '.join(reversed_list)
    return rev_sent # good no to up am I swear solemnly I

sentence = "I solemnly swear I am up to no good"
#print(reverse_sentence(sentence))
#Example Input: sentence = "I solemnly swear I am up to no good"
#Example Output: "good no to up am I swear solemnly I"


# QUESTION FROM BLOOMBERG!!!
def compress_strin(my_str):
    dic = {}
    for c in my_str:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    ans = "".join(f"{c}{dic[c]}" for c in dic)

    if len(ans) < len(my_str):
        return ans
    else:
        return my_str
## OR 

def compress_string(my_str):
    if not my_str:
        return ""
    res = ''
    count = 1
    cur = my_str[0]
    for i in range(1, len(my_str)):
        if my_str[i] == cur:
            count += 1
        else:
            res += cur + str(count)
            cur = my_str[i]
            count = 1
    res += cur + str(count) #After the loop ends, we still need to store the last character's count.


    
    return res if len(res) < len(my_str) else my_str
    

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
#print(compressed_Str) #a5b2c3d1

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
#print(compressed_Str2) #abcde 
# did not convert my_str2 because `a1b1c1d1e1` is double the length



def find_the_needle(haystack, needle):
   return haystack.find(needle) #Returns start index of the first occurrence of substring x in a given string. Returns -1 if x is not in the string.
haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle)) #2

# OR


haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2)) #-1






