def majorityElement(self, nums: List[int]) -> int:
        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

            if hash[num] > (len(nums) / 2):
                return num
