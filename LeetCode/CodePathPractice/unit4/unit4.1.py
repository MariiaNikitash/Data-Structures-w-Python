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
print(reverse_list([1, 2, 3, 4, 5])) #[5, 4, 3, 2, 1]