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
# Time: O()
# Space: O()
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




