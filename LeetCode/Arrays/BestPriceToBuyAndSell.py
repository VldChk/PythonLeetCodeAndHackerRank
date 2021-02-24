class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr = prices[0]
        start_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= pr:
                pr = prices[i]
                continue
            else:
                profit += int(pr - start_price)
                start_price = prices[i]
                pr = prices[i]
        profit += int(pr - start_price)
        return profit
