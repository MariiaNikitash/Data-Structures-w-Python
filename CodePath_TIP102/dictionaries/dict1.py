def lineup(artists, set_times):
    dic = {}
    for i in range(len(artists)):
        dic[artists[i]] = set_times[i]
    return dic
                   

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


# Sesion 1
def total_treasure(treasure_map):
    count = 0
    for key, val in treasure_map.items():
        count+=val
    return count

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

print(total_treasure(treasure_map1)) 

# P2
def can_trust_message(message):
    message_chars = set(message)
    if ' ' in message_chars:
        message_chars.remove(' ')

    return len(message_chars) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))


#P3 
def find_duplicate_chests(chests):
    res = []
    dic = {}
    for num in chests:
        if chests[num] == 1:
            dic[num] 


def find_duplicate_chests(chests):
    res = []
    chest_counts = {}
    for chest in chests:
        chest_counts[chest] = chest_counts.get(chest, 0) + 1
        if chest_counts[chest] == 2:
            res.append(chest)
    return res

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))



def is_balanced(code):
    pass


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

