[
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        res = 0

        for j in range(len(prices)):
            res = max(res,prices[j]-prices[i])
            if prices[i]>prices[j]:
                i=j
        return res
