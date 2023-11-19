class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {} # will be used to store anagrams
        ans = [] # will eventually contain grouped anagrams
        for word in strs: # iterate through every string 
            if tuple(sorted(word)) in dic: # checks if it is already a KEY in dic
                # if it is a key, means there's already 
                # a group of anagrams for this set of characters
                dic[tuple(sorted(word))].append(word) # appends current word to corresponding list of anagrams
            else:
                dic[tuple(sorted(word))] = [word]
                # if sorted tuple is not a key, it creates a New Key
                # and a list containing current word as a VALUE
        for lists in dic.values(): # iterates through the vlues of dic
            ans.append(lists) # ans is a list, in which we append lists of values from dic
        return ans
    


#            keys                values
# dic { ('a', 'e', 't') : ['eat', 'tea', 'ate'],
#       ('a', 'n', 't') : ['tan', 'nat'],
#       ('b', 'a', 't') : ['bat] }


# Input: strs = ['tea', 'eat', 'tan', 'ate', 'nat', 'bat]
# Output:
# ans = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat]]

