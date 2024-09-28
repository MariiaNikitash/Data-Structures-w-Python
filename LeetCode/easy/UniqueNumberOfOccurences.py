class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for num in arr:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        return len(map.values()) == len(set(map.values()))