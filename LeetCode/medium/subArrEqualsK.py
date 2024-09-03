def sub(nums, k):
    count = 0
    n = len(nums)
    #print(n)
    
    for i in range(n):
        #print(i)
        cur_sum = 0
        for j in range(i, n):
            #print(j)
            cur_sum = cur_sum + nums[j]
            print(nums[j])
            #print("cur_sum: ",cur_sum)
            if cur_sum == k:
                count += 1
                print('Add to the count: ', count, "\n")
               
    return count
    
    

res = sub([1,2,3,4], 3)
print(res)
