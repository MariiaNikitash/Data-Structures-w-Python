class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #create another array
        ans = []
        #loop 2 times
        for i in (2):
            #loop in nums
            for n in nums:
                ans.append(n)
        return ans

#  anothr solution in 1 line
#    return nums*2

# or 
#    ans = []
#    ans = nums + nums
#return ans