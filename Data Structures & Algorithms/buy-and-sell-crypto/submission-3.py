class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        max_pro = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                max_pro = max(max_pro, profit)
                j += 1

            else:
                i = j
                j += 1
        return max_pro