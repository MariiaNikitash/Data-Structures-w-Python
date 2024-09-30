# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1, r = n
        while l < r:
            mid = (l + r) // 2

            if isBadVersion(mid):
                #if mid is bad, then there might be prev versions
                # that are bad
                r = mid

            else:
                # if mid is good, then all left before are good, shift left to check right half
                l = mid + 1
        # when l == r we found the first bad version, exit the loop and return r
        return r