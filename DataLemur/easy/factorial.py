# Time Complexity: O(n)
# Space Complexity: O(1)

# Iterative approach is better as the recursive approach
# requires extra space for recursion call stack and overhead
# of recursion calls


def factorial(n):
  i = 1
  fac = 1
  while i <= n:
    fac *= i
    i+=1
  return fac 

