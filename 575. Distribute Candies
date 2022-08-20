# Hashmap solution 
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_count = len(candyType)//2
        different_candies = {}
        for c in candyType:
            if c not in different_candies:
                different_candies[c] = c
        return min(len(different_candies),max_count)
