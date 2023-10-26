class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make a list of the size of nums
        answer = [1]* len(nums)

        # make a list of the size of nums 
        # for the indexes before i
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            # 
            left[i] = left[i-1] * nums[i-1]

        right = [1]* len(nums)
        for j in reversed(range(len(nums)-1)):
            right[j] = right[j+1] * nums[j+1]


        for k in range(len(answer)):
            answer[k] = left[k] * right[k]
        return answer