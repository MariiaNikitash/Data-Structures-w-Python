# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"] 

def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)

        for i in range(len(s)):
            s[i] = stack.pop()