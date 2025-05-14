class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, profit = 0, 0, 0
        
        while right < len(prices):
            if prices[right] > prices[left]:
                if prices[right] - prices[left] > profit:
                    profit = prices[right] - prices[left]
            else:
                left = right
        
            right += 1
        
        return profit