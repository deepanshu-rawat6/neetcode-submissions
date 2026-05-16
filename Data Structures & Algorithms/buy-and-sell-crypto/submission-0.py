class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, maxP, profit = 0, 0, 0

        for j, prices_j in enumerate(prices):
            if prices_j > prices[i]:
                profit = prices_j - prices[i]
            
            while prices[i] > prices_j:
                i += 1
            
            if maxP < profit:
                maxP = profit
        
        return maxP
        