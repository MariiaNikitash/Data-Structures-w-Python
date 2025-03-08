def sum_of_number_strings(nums):
    count = 0
    for s in nums:
        count += int(s)
    return count
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
#print(sum) #60


def remove_duplicates(nums):
    if not nums:
        return nums
    
    cur = nums[0]
    i = 1
    while i < len(nums): # while instead of for bc I can i can pop before i increment avoiding index shifting with for loop approach
        if nums[i] == cur:
            nums.pop(i)
        else:
            cur = nums[i]
            i += 1
    return nums      
nums = [1,1,1,2,3,4,4,5,6,6]
#print(remove_duplicates(nums))
#no_dups = [1,2,3,4,5,6]


def reverse_only_letters(s):
    letter_list = []
    for c in s:
        if c.isalpha():
            letter_list.append(c)
    res = ''
    letter_index = len(letter_list) - 1 # start from the end  

    for c in s:
        if c.isalpha():
            res += letter_list[letter_index]
            letter_index -= 1
        else:
            res += c
    return res

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s) #j-Ih-gfE-dCba


# Time O(n)
# Space O(1) 
def longest_uniform_substring(s):  
    r = 0
    l = 1
    count = 1
    max_count = 1
    while l < len(s):
        if s[r] == s[l]:
            count += 1

        else:
            max_count = max(max_count, count)
            count = 1
            r = l
        l += 1 
    return max(max_count, count)



s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1) #4

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2) #1
