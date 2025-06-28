def lineup(artists, set_times):
    dic = {}
    for i in range(len(artists)):
        dic[artists[i]] = set_times[i]
    return dic
                   

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

#print(lineup(artists1, set_times1))
#print(lineup(artists2, set_times2))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

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

#print(total_treasure(treasure_map1)) 
#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# P2
def can_trust_message(message):
    message_chars = set(message)
    if ' ' in message_chars:
        message_chars.remove(' ')

    return len(message_chars) == 26

# OR
def can_trust_message(message):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    message_letters = set(message)
    return message_letters >= alphabet  # allows extra chars like spaces

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

#print(can_trust_message(message1))
#print(can_trust_message(message2))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

#P3 
def find_duplicate_chests(chests):
    res = []
    dic = {}
    for c in chests:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
            
        if dic[c] == 2:
            res.append(c)
    return res


#def find_duplicate_chests(chests):
#    res = []
#    chest_counts = {}
#    for chest in chests:
#        chest_counts[chest] = chest_counts.get(chest, 0) + 1
#        if chest_counts[chest] == 2:
#            res.append(chest)
#    return res

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

#print(find_duplicate_chests(chests1))
#print(find_duplicate_chests(chests2))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# Problem 4 
# Remove Letter To Equalize Frequency
## Ex: aabbb -> removed b => aabb


def is_balanced(code):
    freq_dic = {}
    for c in code:
        if c in freq_dic:
            freq_dic[c] += 1
        else:
            freq_dic[c] = 1
    
    freq_count = {}
    for c in freq_dic.values():
        if c in freq_count:
            freq_count[c] +=1
        else:
            freq_count[c] = 1
    
    len_freq = len(freq_count)

    if len_freq >= 3:
        return False
    
    if len_freq == 1:
        # Check if all characters are the same or if the frequency is 1, which is a special case
        if len(freq_dic.keys()) == 1:
            return True
        # If all characters have the same frequency, we can remove one to potentially balance the string
        return list(freq_count.keys())[0] == 1
    
    # If there are exactly two unique frequencies
    for val, freq in freq_count.items():
        if val == 1 and freq == 1:
            return True
        
    # Extract 2 unique freqs to check further since no char is == 1
    values = list(freq_count.keys())
    # Check if the difference between the two frequencies is 1 and the higher frequency occurs exactly once
    if values[0] - values[1] == 1 and freq_count[values[0]] == 1:
        return True
    # Check reverse
    if values [1] - values[0] == 1 and freq_count[values[1]] == 1:
        return True
    
    return False

codes = ['aabbc', 'aaabb', 'aabbcc', 'aabbccdde']
for code in codes:
    #print(code, "is", is_balanced(code)) 


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# P6
# Two Sum 
 def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

print(two_sum([2, 7, 8, 5], 7))


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# Problem 7


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# Problem 8