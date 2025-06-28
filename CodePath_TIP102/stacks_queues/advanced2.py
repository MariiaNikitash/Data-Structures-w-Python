# Hakerrank 
def findRestaurant(list1, list2):
    res = []
    dic = {}
    minimum = float('inf')
    for index, val in enumerate(list1):
        dic[val] = index
    
    for j, word in enumerate(list2):
        if word in dic:
            i = dic[word]
            cur_sum = i + j

            if cur_sum < minimum:
                result = [word]
                minimum = cur_sum
            elif cur_sum == minimum:
                result.append(word)
    return result 

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
#print(findRestaurant(list1, list2))


#Problem 2
def build_skyscrapers(floors):
    pass
#print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 



# Problem 3: Dream Corridor Design
def max_corridor_area(segments):
    l,r = 0, len(segments)-1
    max_area = 0
    while l < r:
        area = min(segments[l], segments[r]) * (r-l)
        if segments[l] > segments[r]:
            r-=1
        else:
            l+=1
        if max_area < area:
            max_area = area
    return max_area

#print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
#print(max_corridor_area([1, 1])) 


# Problem 4: Dream Building Layout
def min_swaps(s):
    count = 0
    max_imbalance = 0
    for b in s: 
        if b == '[':
            count-=1
        else:
            count+=1
        max_imbalance = max(max_imbalance, count)

    return (max_imbalance +1) // 2


#print(min_swaps("][][")) #1
#print(min_swaps("]]][[[")) #2
#print(min_swaps("[]"))  #0


# Problem 5: LC: 1249. Minimum Remove to Make Valid Parentheses (medium)
def make_balanced_room(s):
    s = list(s)
    stack = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                s[i] = ''
    while stack:
        s[stack.pop()] = ''

    return ''.join(s)
#print(make_balanced_room("art(t(d)e)sign)")) # art(t(d)e)s)ign
#print(make_balanced_room("d)e(s)ign")) #de(s)ign
#3print(make_balanced_room("))((")) # " "


# Hackerrank 
# Two Sum array is sorted 
def TwoSum(nums, target):
    l,r = 0, len(nums)-1
    while l<r:
        cur_sum = nums[l] + nums[r]
        if target == cur_sum:
            return [l+1, r+1]
        elif cur_sum > target:
            r-=1
        else:
            l+=1
#print(TwoSum([2,7,11,15], 9))


# Top k Largest Element in array
import heapq
def topKlargest(nums, k):
    max_h = [-x for x in nums]
    heapq.heapify(max_h)

    res = []
    for _ in range(min(len(nums), k)):
        largest = -heapq.heappop(max_h)
        res.append(largest)

    return res
print(topKlargest([3,2,1,5,6,4], 2))
print(topKlargest([], 2))


#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 6

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 7