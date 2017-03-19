class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if n == 0:
            return 0
        if n == 1:
            return 0
        f = [0] * n
        buy_price = prices[0]
        temp_buy_price = prices[0]
        for i in range(1,n):
            if prices[i] - buy_price < 0:
                temp_buy_price = prices[i]
            if prices[i] - temp_buy_price > prices[i] - buy_price:
                buy_price = temp_buy_price
                #temp_buy_price = 0
            f[i] =max(max(prices[i] - temp_buy_price,prices[i] - buy_price), f[i-1])
        return f[n-1]

test = Solution()
print test.maxProfit([7,1,5,3,0,6])
