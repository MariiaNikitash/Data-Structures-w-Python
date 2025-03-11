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

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))