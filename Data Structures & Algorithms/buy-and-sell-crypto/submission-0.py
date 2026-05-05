class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        left = 0
        right = 1 

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right

            profit = prices[right] - prices[left]

            if profit > best:
                best = profit
                
            right +=1
        return best