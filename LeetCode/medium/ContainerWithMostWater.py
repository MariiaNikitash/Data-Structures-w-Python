#Time Complexity: O(N), because we need to check the entire range of heights once.
#Space Complexity: O(1), because we only use a constant number of variable to hold our area information.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0 
        while l < r:
            # Area: Width(right index - left) x Height(smaller value)
            area = (r-l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r-= 1
        
        return max_area