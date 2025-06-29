# Letcode Mountain Array
def valid_mtn_arr(arr):
    if len(arr) < 3:
        return False
    
    i = 0
    while i + 1 < len(arr) and arr[i] < arr[i+1]:
        i+=1
    if i == 0 or i == len(arr) -1:
        return False
    while i + 1 < len(arr) and arr[i] > arr[i+1]:
        i+=1
        
    return i == len(arr) - 1

#Input: arr = [2,1]
#Output: False

#Input: arr = [3,5,5]
#Output: false

#Input: arr = [0,3,2,1]
#Output: true


# Prime frequency Map in 2D matrix
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY matrix as parameter.
def prime_frequency_map(matrix):
    dic = {}
    for row in matrix:
        for num in row:
            if is_prime(num):
                if num in dic:
                    dic[num] +=1
                else:
                    dic[num] = 1
                    
    return dic
#Input: matrix = [
#  [1, 4, 7, 11, 15],
#  [2, 5, 8, 12, 19],
#  [3, 6, 9, 16, 22],
#  [10, 13, 14, 17, 24],
#  [18, 21, 23, 26, 30]
#]
#Output: {2: 1, 3: 1, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1}
#
#Input: matrix = [
#  [4, 6, 8],
#  [10, 12, 14]
#]
#Output: {}

# Leetcode Medium 394. Decode String
def decode_string(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop()
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substr)
    
    return "".join(stack)

#Input: s = "3[a]2[bc]"
#Output: "aaabcbc"

#Input: s = "3[a2[c]]"
#Output: "accaccacc"