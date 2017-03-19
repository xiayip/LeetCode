class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                j = nums[i] - 1
                nums[j], nums[i] = nums[i], nums[j]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res



test = Solution()
print test.findDuplicates([4,3,2,7,8,2,3,1])
