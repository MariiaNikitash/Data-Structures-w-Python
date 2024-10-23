class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # base case
        if n == 1:
            return True
        # base case
        if n == 0 or n % 2 != 0:
            return False
        # divide by two
        return self.isPowerOfTwo(n/2)