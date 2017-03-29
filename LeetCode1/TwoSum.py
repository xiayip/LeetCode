class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            r = target-nums[i]
            if nums[i] in res:
                return [nums.index(r), i]
            res.append(r)
        return res

test = Solution()
print test.twoSum([2, 7, 11, 15],9)