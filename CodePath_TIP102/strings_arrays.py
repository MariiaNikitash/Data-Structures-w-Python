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
print(minimum_boxes(meals, capacity))

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
print(wealthiest_customer(accounts))
#Space O(nxm)
#Time O(1)