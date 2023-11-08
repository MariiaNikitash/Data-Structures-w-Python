class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS, mapT = {}, {}
        for index in range (len(s)):
            if s[index] in mapS:
               mapS[s[index]] += 1
            else:
                 mapS[s[index]] = 1
            if t[index] in mapT:
                mapT[t[index]] += 1
            else:
                 mapT[t[index]] = 1
        return mapS == mapT
