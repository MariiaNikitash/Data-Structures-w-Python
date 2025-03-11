# 2 Pointers
#A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n: #
        if n % i == 0:
            return False
        i += 1
    return True

#print(is_prime(5))
#print(is_prime(12))
#print(is_prime(9))


def reverse_list(lst):
    r,l = 0, len(lst) -1
    while r < l:
        temp = lst[r]
        lst[r] = lst[l]
        lst[l] = temp
        r +=1
        l -=1
    return lst
#print(reverse_list([1, 2, 3, 4, 5])) #[5, 4, 3, 2, 1]


def sort_array_by_parity(nums):
    l, r = 0, len(nums) -1
    while l < r:
        if nums[l] % 2 == 0:
            l+=1
        elif nums[r] % 2 == 1:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums)) #[2,4,3,1]
print(sort_array_by_parity(nums2)) #[0]
# Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
