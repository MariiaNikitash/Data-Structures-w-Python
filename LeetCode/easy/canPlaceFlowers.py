class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # created new list with zeros at the end and beginning
        # so i can check if the first n last elem is 0
        newList = [0] + flowerbed + [0]
        for index in range(1, len(newList)-1):
            # if 3 positions are 0 
            if newList[index-1] == 0 and newList[index] == 0 and newList[index+1] == 0:
                # place a flower
                newList[index] = 1
                n-=1
        return n <= 0
    
