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
print(first_unique_char(my_str))#0

str2 = "loveleetcode"
print(first_unique_char(str2)) #2

str3 = "aabb"
print(first_unique_char(str3)) #-1