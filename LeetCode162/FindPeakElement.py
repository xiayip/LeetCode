class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums) - 1
        return self.findPeak(nums,1,len(nums)-1)

    def findPeak(self, nums, s, e):
        im = (e-s) // 2 +s
        if nums[im-1] < nums[im]: #
            if nums[im] > nums[im+1]:
                return im
            else: # search the right
                return self.findPeak(nums, im, e)
        else:
            # search the left part
            return self.findPeak(nums,s, im)


test = Solution()
print test.findPeakElement([ 2, 3, 4, 5, 6])

