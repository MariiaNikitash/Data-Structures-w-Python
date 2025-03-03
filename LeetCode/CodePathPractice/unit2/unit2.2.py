def student_directory(student_names):
    dic = {}
    for i, name in enumerate(student_names):
        dic[i] = name
    return dic
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
#Example Output: {"Ada Lovelace": 1, "Tu Youyou": 2, "Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 5}
#print(student_directory(student_names))

def get_description(info, keys):
    for key in keys:
        if key in info:
	        print(info[key])
        else:
            print("None")
         
    
   
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
#print(get_description(info, keys))



def sum_even_values(dictionary):
    count = 0
    for even in dictionary.values():
        if even % 2 == 0:
            count += even
    return count
    

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
#print(sum_even_values(dictionary))


def merge_catalogs(catalog1, catalog2):
    for product, price in catalog2.items():
        catalog1[product] = price
    return catalog1

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
#print(merge_catalogs(catalog1, catalog2))#{"apple": 1.0, "banana": 0.75, "cherry": 1.25}


def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    return votes

votes = {"Alice": 5, "Bob": 3}

#print(cast_vote(votes, "Alice"))
#print(cast_vote(votes, "Gina"))

#{"Alice": 6, "Bob": 3}
#{"Alice": 6, "Bob": 3, "Gina": 1}


#Write a function that takes in two dictionaries,
#dict1 and dict2 and finds all keys common to both
#dictionaries. The function returns a list of common keys.


def common_keys(dict1, dict2):
    lst = []
    for common in dict1:
        if common in dict2:
            lst.append(common)
    return lst
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
#print(common_list) #['b', 'c']



def count_occurrences(nums):
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    return dic
nums = [1, 2, 2, 3, 3, 3, 4] 
#xample Output: {1: 1, 2: 2, 3: 3, 4: 1} 
#print(count_occurrences(nums))


#def get_highest_priority_task(tasks):
# ?????


def find_majority_element(nums):
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

        if dic[num] > (len(nums) / 2):
            return num
        
     

nums = [2, 2, 1, 1, 1, 2, 2]
#print(find_majority_element(nums))
#Example Output: 2


def hasDuplicates(nums, k):
    recent_index = {}  # Dictionary to store the last index of each number
    for i in range(len(nums)):
        if nums[i] in recent_index:  # Check if we've seen this number before
            diff = i - recent_index[nums[i]]  # Calculate the difference between indices
            if diff < k:  # If the difference is within k, return True
                return True
        recent_index[nums[i]] = i  # Update the most recent index of this number
    return False

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 5)
print(check2)
#Example Output:
#False
#True
