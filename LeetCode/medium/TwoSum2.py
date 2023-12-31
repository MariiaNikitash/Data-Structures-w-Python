class Solution:
    def twoSum(numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            answer = numbers[l] + numbers[r]
            if answer > target:
                r-=1
            elif answer < target:
                l+=1
            else:
                return [l+1, r+1]
    



# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]