class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        f = []
        f.append([0])
        f.append(max(nums[0],nums[1]))
        for i in range(2,n):
            f.append(max(f[i-2] + nums[i], f[i-1]))
        return f[n-1]


test = Solution()
print test.rob([1,1,1])
