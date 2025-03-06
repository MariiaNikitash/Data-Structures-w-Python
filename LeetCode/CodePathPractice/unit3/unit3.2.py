def sum_of_number_strings(nums):
    count = 0
    for s in nums:
        count += int(s)
    return count
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
#print(sum) #60


def remove_duplicates(nums):
    if not nums:
        return nums
    
    cur = nums[0]
    i = 1
    while i < len(nums): # while instead of for bc I can i can pop before i increment avoiding index shifting with for loop approach
        if nums[i] == cur:
            nums.pop(i)
        else:
            cur = nums[i]
            i += 1
    return nums

       

      
nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
#no_dups = [1,2,3,4,5,6]