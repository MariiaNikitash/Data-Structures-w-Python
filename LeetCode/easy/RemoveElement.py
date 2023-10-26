class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #l is a left pointer is at index 1 bc index 0 obviosly 1st so its unique
        l = 1

        #r is a right pointer, goes from index 1 to len(nums)
        for r in range(1, len(nums)):
            #if right index in not equal to the previous index
            if nums[r] != nums[r-1]:
                #then l = r
                nums[l] = nums[r]
                #we have to increment l so int continues to search for the unique values
                l += 1
        return l
