#Problem 1: Balanced Art Collection
#A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.
#Ret len of longest subsequence 
#Time: O(n)
#Space: O(n)

def find_balanced_subsequence(art_pieces):
    dic = {}
    for num in art_pieces:
        if num in dic:
            dic[num] +=1
        else:
            dic[num] =1
    max_len = 0
    for num in dic:
        if num+1 in dic:
            cur_len = dic[num] + dic[num + 1]
            max_len = max(max_len, cur_len)
    return max_len


art_pieces1 = [1,3,2,2,5,2,3,7] # Output: 5  so [3,2,2,2,3] is the longest subsequence of adj nums
art_pieces2 = [1,2,3,4] # 2
art_pieces3 = [1,1,1,1] # 0

#print(find_balanced_subsequence(art_pieces1))
#print(find_balanced_subsequence(art_pieces2))
#print(find_balanced_subsequence(art_pieces3))


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# #Problem 2: Verifying Authenticity
# The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it 
# array of length n + 1 containing the integers from 1 to n - 1 exactly once, and int n twice. Ex: base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

#Write a func that accepts arr of integers art_pieces and returns True if given array is authentic array, else False.
def is_authentic_collection(art_pieces):
    n = max(art_pieces)
    if len(art_pieces) != n+1: # bc nums are ordered, no skips so biggest num should appear twice
        return False
    
    counts = {}
    for num in art_pieces:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for i in range(1, n):
        if counts.get(i, 0) == 1:
            return True
    
    return counts.get(n, 0) == 2
    



collection1 = [2, 1, 3] # F
collection2 = [1, 3, 3, 2] # T
collection3 = [1, 1] # T

#print(is_authentic_collection(collection1))
#print(is_authentic_collection(collection2))
#print(is_authentic_collection(collection3))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# #Problem 3:
def organize_exhibition(collection):
    result = []
    counts = dict()
    for item in collection:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    maxx = 0
    for item in counts.keys():
        maxx = max(counts[item], maxx)

    for i in range(maxx):
        result.append(set())

    for item in counts.keys(): 
        for i in range(counts[item]): 
            result[i].add(item)

    for i in range(len(result)):
        result[i] = list(result[i])
    return result

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

#print(organize_exhibition(collection1))
#print(organize_exhibition(collection2))

# Or 

def findMatrix(nums):
    count = {}
    res = []

    for n in nums:
        # Step 1: Determine row by checking and initializing manually
        if n in count:
            row = count[n]
        else:
            row = 0

        # Step 2: Create new row if needed
        if len(res) == row:
            res.append([])

        # Step 3: Add the number to the correct row
        res[row].append(n)

        # Step 4: Increment the count manually
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    return res
    

nums = [1,3,4,1,2,3,1]
#print(findMatrix(nums))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# Hackerrank 
# Roman to Integer
def romanToInt(s):
    res = 0
    dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    for i in range(len(s)):
        if i+1 < len(s) and dic[s[i]] < dic[s[i+1]]:
            res -= dic[s[i]]
        else:
            res += dic[s[i]]
    return res

s = "III" # 3
s1 = "CMXCVIII" # 998 so C<M so res=-100, then M>X so res = 900, then X<C so res=890, C<V so res=990, then V>I so res=995 then +1 +1+1 = 998
#print(romanToInt(s1))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# #Problem 4
def subdomain_visits(cpdomains):
    visit_count = {}
    res = []
    #split count and domain 
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        fragments = domain.split('.')

        #make subdomains and count visits
        for i in range(len(fragments)):
            subdomain = '.'.join(fragments[i:])
            if subdomain in visit_count:
                visit_count[subdomain] += count
            else:
                visit_count[subdomain] = count
    for domain, count in visit_count.items():
        res.append(f"{count} {domain}")
    return res


#print(subdomain_visits(["900 abstract.gallery.com", "50 impressionism.com", 
#              "1 contemporary.gallery.com", "5 medieval.org"]))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# #Problem 5 # REVISE!!!
def beauty_sum(collection):
    total_beauty = 0
    
    # Generate all substrings
    for i in range(len(collection)):
        freq = {}
        for j in range(i, len(collection)):
            char = collection[j]
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            
            # Calculate the beauty of the current substring
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            
            total_beauty += (max_freq - min_freq)
    
    return total_beauty

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# Problem 6