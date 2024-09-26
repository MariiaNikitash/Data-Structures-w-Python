# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            # or if i do it in one line I dont have to use temp variable
            #s[l],s[r]  = s[r], s[l]
            

            l += 1
            r -= 1