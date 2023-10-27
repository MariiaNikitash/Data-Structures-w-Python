class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for index in nums:
            if index in my_set:
                return True
            
            elif index not in my_set:
                my_set.add(index)
        return False