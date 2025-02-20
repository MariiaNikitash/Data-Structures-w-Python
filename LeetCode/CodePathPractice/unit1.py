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