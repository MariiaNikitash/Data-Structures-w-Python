class Solution:
    def isPalindrome(self, s: str) -> bool:
        new =''
        for f in s: 
            if f.isalnum():
                new+=f.lower()
        return new == new[::-1]