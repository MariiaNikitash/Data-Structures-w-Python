# Review Chapter 4 (Lists, Dicts, Stacks and Queues)
# Advanced Problem Set Version 1
# Focus on Asymptotic Analysis

# Problem 1: Brand Filter
# Time: O(n) brands x 
# Space: O(n)
def filter_sustainable_brands(brands, criterion):
    res = []
    for brand in brands:
        if criterion in brand['criteria']:
            res.append(brand['name'])
    return res

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]
brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]
#print(filter_sustainable_brands(brands, "eco-friendly")) # ['EcoWear', 'GreenThreads']
#print(filter_sustainable_brands(brands_2, "ethical labor")) #['Earthly']
#print(filter_sustainable_brands(brands_3, "carbon-neutral")) ['GreenLife']


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 2: Eco-Friendly Materials
# Time: O(n × m) where m = average materials per brand
# Space: O(n)

def count_material_usage(brands):
    dic = {}
    for brand in brands:
        for material in brand['materials']:
            if material in dic:
                dic[material] +=1
            else:
                dic[material] =1
    return dic

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}]
brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}]
brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}]
#print(count_material_usage(brands)) #{'organic cotton': 2, 'recycled polyester': 2, 'bamboo': 2}
#print(count_material_usage(brands_2)) #{'hemp': 2, 'linen': 2, 'organic cotton': 1, 'recycled wool': 1}
#print(count_material_usage(brands_3)) #{'organic cotton': 1, 'recycled polyester': 2, 'hemp': 1, 'bamboo': 1}


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 3: Fashion Trends
# Time: O(nxm) if m is small then its constant 
# Space: O(n)
def find_trending_materials(brands):
    res = []
    dic = {}
    for brand in brands:
        for material in brand['materials']:
            if material in dic:
                dic[material] +=1
            else:
                dic[material] =1
    for key, val in dic.items():
        if val > 1:
            res.append(key)
    return res
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}]
brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}]
brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}]
#print(find_trending_materials(brands)) # ['organic cotton', 'recycled polyester', 'bamboo']
#print(find_trending_materials(brands_2)) # ['hemp', 'linen']
#print(find_trending_materials(brands_3)) # ['recycled polyester']


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 4: Fabric Pairing
# Time: O(nlogn)
# Space: O(1)
def find_best_fabric_pair(fabrics, budget):
    fabrics.sort(key=lambda x: x[1])
    l,r = 0, len(fabrics ) -1
    best_pair = ()
    closest_sum = 0
    while l <r:
        cost_sum = fabrics[l][1] + fabrics[r][1]
        if cost_sum > closest_sum and cost_sum <= budget:
            closest_sum = cost_sum
            best_pair = (fabrics[l][0], fabrics[r][0])
        if cost_sum > budget:
            r-=1
        else:
            l+=1
    return best_pair



fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

#print(find_best_fabric_pair(fabrics, 45)) #('Hemp', 'Organic Cotton')
#print(find_best_fabric_pair(fabrics_2, 70)) #('Tencel', 'Recycled Wool')
#print(find_best_fabric_pair(fabrics_3, 60)) # ('Bamboo', 'Linen')

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 5: Fabric Stacks
# Time: O(nlogn)
# Space: O(n)

def organize_fabrics(fabrics):
    fabrics.sort(key=lambda x: x[1], reverse=True)
    res = []
    for f in fabrics:
        res.append(f[0])
    return res

fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

#print(organize_fabrics(fabrics))
#print(organize_fabrics(fabrics_2))
#print(organize_fabrics(fabrics_3))
['Hemp', 'Organic Cotton', 'Bamboo', 'Recycled Polyester']
['Recycled Wool', 'Tencel', 'Organic Cotton', 'Linen']
['Hemp', 'Bamboo', 'Recycled Polyester', 'Linen']

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 6:  Supply Chain
# Time: O(nlogn)
# Space: O(n)
from collections import deque
def process_supplies(supplies):
    supplies.sort(key=lambda x: x[1], reverse=True)
    res = []
    q = deque(sup[0] for sup in supplies)
    while q:
        res.append(q.popleft())
    return res

supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

#print(process_supplies(supplies))
#print(process_supplies(supplies_2))
#print(process_supplies(supplies_3))

['Bamboo', 'Organic Cotton', 'Recycled Polyester', 'Hemp']
['Recycled Wool', 'Organic Cotton', 'Tencel', 'Linen']
['Recycled Polyester', 'Linen', 'Hemp', 'Bamboo']

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 7:  Calculate Fabric Waste
# Time: O()
# Space: O()

def calculate_fabric_waste(items, fabric_rolls):
    res = 0
    for i in range(len(items)):
        _, item_len = items[i]
        roll_len = fabric_rolls[i]
        waste = roll_len - item_len
        res += waste
    return res



items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls = [5, 5, 5]
items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls = [4, 4, 4]
items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls = [7, 5, 5]
#print(calculate_fabric_waste(items, fabric_rolls)) 
#print(calculate_fabric_waste(items_2, fabric_rolls)) 
#print(calculate_fabric_waste(items_3, fabric_rolls)) 
