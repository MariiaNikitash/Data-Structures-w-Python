class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1
                j +=1
            else:
                j +=1
        # if we reached th end of str s, for every char in the
        # string we were able to find a matching char in t
        return True if i == len(s) else False