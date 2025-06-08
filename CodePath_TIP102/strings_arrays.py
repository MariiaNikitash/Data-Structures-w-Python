# In Class Solutions 
def greeting(name):
	print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
	
#greeting("Masha")

def get_item(items, x):
    for i in range (len(items)):
        if i == x:
            return items[i]
        
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
#print(get_item(items, x))

def sum_honey(hunny_jars):
    sum = 0
    for num in hunny_jars:
         sum += num
    return sum
hunny_jars = [2, 3, 4, 5]
#print(sum_honey(hunny_jars))
hunny_jars = []
#print(sum_honey(hunny_jars))

def doubled(hunny_jars):
	return [num*2 for num in hunny_jars]
hunny_jars = [1, 2, 3]
#print(doubled(hunny_jars))

def count_less_than(race_times, threshold):
    count = 0
    for num in race_times:
        if num < threshold:
            count +=1
    return count
          

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
#print(count_less_than(race_times, threshold))

def print_todo_list(task):
    print("Pooh's To Dos:\n")
    for i in range(len(task)):
         print(f"{i+1} . {task[i]}")
    
        
        
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
#print_todo_list(task)
task = []
#print_todo_list(task)





def words_with_char(words, x):
    l= []
    for i, char in enumerate(words):
        if x in char:
            l.append(i)
    return l
              
words = ["batman", "superman"]
x = "a"
#print(words_with_char(words, x))


def hulk_smash(n):
    answer = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("HulkSmash")
        elif i % 3 == 0:
            answer.append("Hulk")
        elif i % 5 == 0:
            answer.append("Smash")
        else:
            answer.append(str(i))
    return answer
        
            

n = 15
#print(hulk_smash(n))


def shuffle(message, indices):
    l = [""] * len(message) 
    count = 0
    for index in indices:
        l[index] = message[count]
        count +=1
    return ''.join(l)
message = "evil"
indices = [3, 1, 2, 0]
#print(shuffle(message, indices))



def shuffle(message, indices):
    # Initialize a list to store the shuffled characters
    shuffled_message = [''] * len(message)
    
    for i in range(len(message)):
        index= indices[i]
        char = message[i] 
        shuffled_message[index] = char
    
    # Join the list into a string and return it
    return ''.join(shuffled_message)


# Problem 4
def minimum_boxes(meals, capacity):
    capacity.sort(reverse=True)
    sum_meals = sum(meals)
    boxes = 0
    for spot in capacity:
        if sum_meals <=0:
            break
        sum_meals -=spot
        boxes +=1
    return boxes


meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
#print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
#print(minimum_boxes(meals, capacity))


def wealthiest_customer(accounts):
    richest = 0
    max_sum = 0
    for customer, money in enumerate(accounts):
        current_sum = sum(money)
        if current_sum > max_sum:
            max_sum = current_sum
            richest = customer
    return [richest, max_sum]



accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
#print(wealthiest_customer(accounts))
#Space O(nxm)
#Time O(1)

#Problem 6: Smaller Than
def smaller_than_current(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[i] > nums[j]:
                count +=1
        result.append(count)
    return result
#Time O(n^2), Space O(N) bc result will contain all n values of smaller chars that n   
nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

#Diagonal Sum
def diagonal_sum(grid):
    res = 0
    n = len(grid)
    for i in range(n):
        res+=grid[i][i]
        res+=grid[i][n-1-i]
    
    if n % 2 == 1:
        center = grid[n // 2][n // 2]
        res -= center
    return res

grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(diagonal_sum(grid))
# SESSION 2

def transpose(matrix):
   row = len(matrix)
   col = len(matrix[0])
   result = [[0] * row for _ in range(col)]

   for r in range(row):
       for c in range(col):
           result[r][c] = matrix[r][c]
   return result
#Time/Space O(m * n)   

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#print(transpose(matrix))

def reverse_list(lst):
    p1 = 0
    p2 = len(lst) - 1

    while p1 < p2:
        lst[p1],lst[p2] = lst[p2], lst[p1]
        p1+=1
        p2-=1
    return lst
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
#print(reverse_list(lst))



def remove_dupes(items):
    l = 0
    while l < len(items)-1:
        if items[l] == items[l+1]:
            items.pop(l+1)
        else:
            l+=1
    return items


items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
#print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
#print(remove_dupes(items))



# in 2 ptrs use if-elif block bc i only want to execute 1 line 
def sort_by_parity(nums):
    l = 0
    r = len(nums) -1
    while l<r:
        if nums[l] % 2 == 0:
            l+=1
        elif nums[r] % 2 == 1:
            r-=1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    return nums

#O(n) time, O(1) space
nums = [3, 1, 2, 4]
#print(sort_by_parity(nums))

nums = [0]
sort_by_parity(nums)


# Container with most water
def most_honey(height):
    max_area = 0
    l,r = 0, len(height)-1
    while l < r:
        area = (r-l) * min(height[l], height[r])
        max_area = max(max_area, area)
        if height[r] > height[l]:
            l +=1
        else:
            r-=1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#print(most_honey(height))


# Merge Intervals
#Problem 6: Merge Intervals
#Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key= lambda x: x[0])
    merged = [intervals[0]] #[1,3]
    for start, end in intervals[1:]:
        # Get the end of the last merged interval
        last_end = merged[-1][1] #3
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            intervals.append([start,end])
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
#print(merge_intervals(intervals))

#hackerrank 
#Needle
def find_needle(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) +1):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1

# can place flowers
# Sliding window 
def canPlaceFlowers(flowerbed, n):
    flowerbed = [0] + flowerbed + [0]
    count = 0

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1

    return count >= n