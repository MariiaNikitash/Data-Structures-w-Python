# Linear Search 
def linear_search(lst, target):
    for i, num in enumerate(lst):
        if num == target:
            return i
    return -1


lst = [1,4,5,2,8]
position = linear_search(lst,5)
#print(position) # returns 2 (index of 5)


def print_indices(lst):
    for i in range(len(lst)):
        print(i)

lst = [5,1,3,8,2]
#print_indices(lst)


def fizzbuzz(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        #if num % 3 != 0 or num % 5 != 0:
        else:
            print(num)
#fizzbuzz(15)


def find_divisors(n):
    lst = []
    for num in range(1, n+1):
        if n % num == 0:
            lst.append(num)
    return lst

lst = find_divisors(6)
#print(lst)
#Example Output:
#[1, 2, 3, 6]

def multiples_of_five():
    for num in range(5, 101, 5): # Start from 5, go up to 100, step by 5
        print(num)
#multiples_of_five()

def get_evens(lst):
    l = []
    for num in lst:
        if num % 2 == 0:
            l.append(num)
    return l

lst = [1,2,3,4]
evens_lst = get_evens(lst)
#print(evens_lst) -> [2,4]

# in-place
def get_evens(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            lst.pop(i)
        else:
            i +=1
    return lst


lst = [1,2,3,4]
evens_lst = get_evens(lst)
#print(evens_lst) # [2,4]

def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count +=1
    return count
numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
#print(counter) # 3


def max_difference(lst):
    if len(lst) < 2:
        return 0
    min,max = lst[0], lst[0]
    for num in lst:
        if num < min:
            min = num
        if num > max:
            max = num
            
    return max - min

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
#print(max_diff) # 20


def flip_sign(lst): 
    l = []
    for num in lst:
        new = num * (-1)
        l.append(new)
    return l



lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
#print(flipped_lst) #[-1, 2, 3, -4]

def doubled(lst):
    for num in lst:
        print(num*2)
lst = [1,2,3] # 2 4 6
#doubled(lst)

def doubled(lst):
    return lst + lst
lst = [1,2,3] # [1,2,3,1,2,3]
#print(doubled(lst))

def print_list(lst):
    for s in lst:
        print(s)
#print(print_list(["squirtle", "gengar", "charizard", "pikachu"])) 

def convertTemp(celsius):
    ans = []
    K = celsius + 273.15
    F = celsius * 1.80 + 32.00
    ans.append(K)
    ans.append(F)
    return ans

temperatures = convertTemp(23.00)
#print(temperatures) #[296.15, 73.40]

def average(scores):
    count = 0
    for num in scores:
        count += num
    return count / len(scores)

scores = [84,73,92,95,88]
avg_score = average(scores)
#print(avg_score) #86.4

def increment_values(lst):
    l = []
    for num in lst:
        new = num + 1
        l.append(new)
    return l
lst = [3,5,8,2]
new_lst = increment_values(lst)
#print(new_lst) # [4, 6, 9, 3]

def check_num(lst, num):
    for n in lst:
        if n == num:
            return True
    return False
lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
#print(flag1)
#rint(flag2)
#Example Output: flag1 == True and flag2 == False


def find_missing(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
#print(missing_num) #3

def reverse_list(lst):
    l = []
    for num in reversed(lst):
        l.append(num)
    return l

# or 
def reverse_list(lst):
    return lst[::-1]

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
#print(rev_lst) ##[5,4,3,2,1]

def get_odds(nums):
    l = []
    for num in nums:
        if num % 2 == 1:
            l.append(num)
    return l
nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
#print(odd_nums) #[5, 1, 5]


def multiplication_table(num):
    for n in range(1,11):
        print (n * num)
#print(multiplication_table(7)) 

def list_to_number(digits):
    if len(digits) == 0:
        return 0
    num = 0
    for d in digits:
        num = num * 10 + d
    return num
digits = [1,0,3]
number = list_to_number(digits)
#print(number) #103

def move_zeroes(nums):
    l = []
    zeros = 0
    for num in nums:
        if num == 0:
            zeros +=1
        else:
            l.append(num)

    for z in range(zeros):
        l.append(0)
    return l

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
#print(new_nums) #[1,2,3,4,0,0,0]

def print_odd_indices(nums):
    for i in range(len(nums)):
        if i % 2 == 1:
            print(nums[i])

nums = [3,4,8,1,5,2]
#print_odd_indices(nums) # 4 1 2

def find_all_occurrences(lst, target):
    l = []
    for i in range(len(lst)):
        if target == lst[i]:
            l.append(i)
    return l
lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list) #[1,4,7,8]