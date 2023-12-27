class Solution:
    def maxProfit(self, prices):
        if not prices and len(prices) == 1:
            return 0
        
        # assume first element is min price in the given prices
        min_price = prices[0]
        max_profit = 0

        # Iterate through all prices from second element
        for curr_price in prices[1:]:
            # update max profit
            max_profit = max(max_profit, curr_price - min_price)
            # update min price
            min_price = min(min_price, curr_price)
        
        return max_profit
        

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    obj = Solution()
    res = obj.maxProfit(prices)
    print(res)