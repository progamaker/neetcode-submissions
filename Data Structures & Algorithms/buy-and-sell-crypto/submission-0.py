class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        profit = 0
        min_value= 10000
        for i in range(len(prices)):
            min_value= min(min_value,prices[i])
            profit = prices[i] - min_value
            ans = max(ans,profit)
        return ans