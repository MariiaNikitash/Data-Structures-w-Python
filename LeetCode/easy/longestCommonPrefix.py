
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # iterate over each char in the first string
        for i in range(len(strs[0])):
            # iterate over each string in strs
            for s in strs:
                # check if i is the last index in s or if char in s is different from char in strs
                if i == len(s) or s[i] != strs[0][i]: 
                    return res
            # If the inner loop completes without returning, it means the character at position i is
            #  the same across all strings. In that case, the character strs[0][i] is appended to res
            res += strs[0][i]
        return res
