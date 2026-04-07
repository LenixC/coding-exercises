class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_sale = 0

        while i < len(prices):
            j = i + 1 
            while j < len(prices):
                max_sale = max(max_sale, prices[j]-prices[i])
                j += 1
            i += 1
        
        return max_sale
            
