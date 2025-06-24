# Review Chapter 4 (Lists, Dicts, Stacks and Queues)
# Focus on Asymptotic Analysis

# Problem 1: NFT Name Extractor
# Time: O(n)
# Space: O(n)
def extract_nft_names(nft_collection):
    res = []
    for nft in nft_collection:
        res.append(nft['name'])
    return res

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Abstract Horizon", "creator": "DreamyPixel", "value": 3.8}
]
#print(extract_nft_names(nft_collection))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 2: NFT Collection Review
# Time: O(n)
# Space: O(n)
def extract_nft_nmes(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

#print(extract_nft_nmes(nft_collection))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 3: Identify Popular Creators
# Time: O(n)
# Space: O(n)
def identify_popular_creators(nft_collection):
    dic = {}
    res = []
    for nft in nft_collection:
        name = nft["name"]
        if name in dic:
            dic[name] +=1
        else:
            dic[name] = 1
    
    for name, count in dic.items():
        if count > 1:
            res.append(name)
    return res
#print(identify_popular_creators(nft_collection))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 4: NFT Collection Statistics
# Time: O(n)
# Space: O(1)
def average_nft_value(nft_collection):
    if not nft_collection:
        return 0
    avarage = 0
    for val in nft_collection:
        avarage += val['value']
    return round(avarage / len(nft_collection), 2)

#print(average_nft_value(nft_collection))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 5: NFT Tag Search
# Time: O(n*m)
# Space: O(n)
def search_nft_by_tag(nft_collections, tag):
    res = []
    for collection in nft_collections:
        for nft in collection:
            if tag in nft["tags"]:
                res.append(nft["name"])
    return res


nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]
#print(search_nft_by_tag(nft_collections_2, "sunset"))


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 6: NFT Queue Processing
# Time: O(n)
# Space: O(n)

def process_nft_queue(nft_queue):
    res = []
    for dic in nft_queue:
        res.append(dic["name"])
    return res


# OR using Deque for FIFO 
# Time: O(n)
# Space: O(n)
from collections import deque
def process_nft_queue(nft_queue):
    res = []
    q = deque(nft_queue)

    while q:
        nft = q.popleft()
        res.append(nft["name"])
    return res

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
#print(process_nft_queue(nft_queue)) # ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 7: Validate NFT Addition
# Time: O(n)
# Space: O(n)

def validate_nft_actions(actions):
    if not actions:
        return True
    stack = []
    for action in actions:
        if action == 'add':
            stack.append(action)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

#print(validate_nft_actions(actions)) # T
#print(validate_nft_actions(actions_2)) # T
#print(validate_nft_actions(actions_3)) # F

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
#Problem 7: Validate NFT Addition
# Time: O(log(n))
# Space: O(1)
def find_closest_nft_values(nft_values, budget):
    l,r = 0, len(nft_values)-1
    closest_below, closest_above = None, None
    while l <= r:
        mid = (l+r) // 2
        if nft_values[mid] == budget:
            return nft_values[mid], nft_values[mid]
        elif nft_values[mid] < budget:
            closest_below = nft_values[mid]
            l = mid+1
        else:
            closest_above = nft_values[mid]
            r = mid-1
    return closest_below, closest_above




nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0)) # (7.2, 9.0)
print(find_closest_nft_values(nft_values_2, 6.5)) # (6.3, 7.8)
print(find_closest_nft_values(nft_values_3, 3.0)) # (2.5, 4.0)

