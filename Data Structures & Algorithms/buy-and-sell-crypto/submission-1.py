class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minmBuy = float("inf")

        for price in prices:
            if price < minmBuy:
                minmBuy = price
            maxP = max(maxP, price - minmBuy)
        return maxP


        