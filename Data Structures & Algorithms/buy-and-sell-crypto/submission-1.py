class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_difference = 0
        lowest_seen = prices[0]
        
        for i in range(1 ,len(prices)):
            if prices[i] < lowest_seen:
                lowest_seen = prices[i]
            elif prices[i] > lowest_seen and prices[i] - lowest_seen > highest_difference:
                highest_difference = prices[i] - lowest_seen
        
        return highest_difference