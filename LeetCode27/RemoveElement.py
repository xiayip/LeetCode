class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        return len(nums) - nums.count(val)


test = Solution()
print test.removeElement([3,2,2,3],3)
# a = [1,2,3]
# print a.count(4)