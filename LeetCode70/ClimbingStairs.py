class Solution(object):

    # back tracking method
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     self.count = 0
    #     self.backTracking(n)
    #     return self.count
    #
    # def backTracking(self, n):
    #     if n < 0:
    #         return
    #     if n == 0:
    #         self.count = self.count + 1
    #         return
    #     for i in [1,2]:
    #         self.backTracking(n-i)

    # dp method
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+2)]
        dp[1] = 1
        dp[2] = 2
        for i in range(2, n+2):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n+1]


test = Solution()
print test.climbStairs(35)