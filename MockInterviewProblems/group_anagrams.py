from collections import defaultdict

def get_key(word):
    # Create a list with 26 zeroes — one for each letter from 'a' to 'z'
    letter_count = [0] * 26

    # Count how many times each letter appears in the word
    for char in word:
        index = ord(char) - ord('a')  # 'a' → 0, 'b' → 1, ..., 'z' → 25
        letter_count[index] += 1

    # Convert the list of numbers to a string (because lists can't be dict keys)
    return tuple(letter_count)

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = get_key(word)  # This is the letter count signature
        groups[key].append(word)

    return list(groups.values())

# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))