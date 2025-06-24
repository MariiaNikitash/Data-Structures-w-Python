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
print(process_nft_queue(nft_queue)) # ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']