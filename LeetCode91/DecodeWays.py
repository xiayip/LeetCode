class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,len(s)):
            if 9<10*int(s[i-1])+int(s[i])<=26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[len(s)-1]

test = Solution()
print test.numDecodings('121242351242521')