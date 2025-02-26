def is_subsequence(lst, sequence):
    seq_idx = 0
    for num in lst:
        if sequence[seq_idx] == num:
            seq_idx += 1
        if seq_idx == len(sequence):
            return True
    return False


lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
#print(is_subsequence(lst, sequence)) # True


def create_dictionary(keys, values):
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]

    return dic

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
#print(create_dictionary(keys, values))


def print_pair(dic, target):
    if target not in dic:
        print(" That pair does not exist!")
    else:
        print(" Key: ", target,"\n",
              "Value: ", dic[target])

#dic = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
#print_pair(dic, "patrick")
#print_pair(dic, "plankton")
#print_pair(dic, "spongebob")
# Key: patrick
# Value: star
# That pair does not exist!
# Key: spongebob
# Value: squarepants

def keys_v_values(dict):
    v = 0
    k = 0
    for key in dict:
        k += key
        v += dict[key]
    if k > v:
        return "keys"
    else:
        return "values"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
#print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
#print(greater_sum)
#values
#keys



def restock_inventory(current_inventory, restock_list):
    for item, quantity in restock_list.items():
        if item in current_inventory:
            current_inventory[item] += quantity
        else:
            current_inventory[item] = quantity
    return current_inventory

current_invent = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}
restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
#print(restock_inventory(current_invent, restock_list)) # {'apples': 40, 'bananas': 15, 'oranges': 30, 'pears': 5}



def calculate_gpa(report_card):
    grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    if not report_card:
        return 0.0
    
    count = 0
    for grade in report_card.values():
        points = grade_points[grade]
        count += points
    gpa = count / len(report_card)
    return round(gpa, 2)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
#Example Output: 3.33