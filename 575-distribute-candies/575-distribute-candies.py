class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
         return int(min(len(candyType) / 2, len(set(candyType))))
        