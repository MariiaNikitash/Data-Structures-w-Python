# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# NOT OPTIMIZED SOLUTION
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(0, len(nums)):
            for index2 in range(1, len(nums)):
                if index1 != index2 and nums[index1] + nums[index2] == target:
                    return index1, index2
                
# Optimized Soulution using a map, which stores value and index of the complement 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary to store numbers and their indices
        map = {} # val : index
        # Iterate over the list using both index (i) and value (num)
        for index, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], index]
             # If complement doesn't exist, store the current number and its index in the dictionary
            map[num] = index