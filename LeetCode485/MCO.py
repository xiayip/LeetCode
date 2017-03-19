class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_p = 0
        cnt = 0
        max_len = 0
        for n in nums:
            if n == 1:
               cnt += 1
            else:
                cnt = 0
            max_len = max(max_len,cnt)
        return max_len



test = Solution()
print test.findMaxConsecutiveOnes([1,1,0,1,1,1])