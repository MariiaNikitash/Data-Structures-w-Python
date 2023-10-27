class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make a list of the size of nums
        answer = [1] * len(nums)

        # make a list of the size of nums 
        # for the indexes before i
        left = [1] * len(nums)
        #start at index 1 because thers no elems before index 0
        for index in range(1, len(nums)):
            # so index = 
            left[index] = left[index-1] * nums[index-1]

        # same here do list for right = [1,1,1,1]
        right = [1]* len(nums)

        # since we need multiply all indexes to the right of index 
        # we do reverse loop and start at the second to last index
        for index in reversed(range(len(nums)-1)):
            right[index] = right[index+1] * nums[index+1]

        # loop to multiply index of left with index of right
        for index in range(len(answer)):
            answer[index] = left[index] * right[index]
        return answer
    


