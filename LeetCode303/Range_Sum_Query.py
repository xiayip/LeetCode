class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num_len = len(nums)
        self.nums = nums
        self.sum = 0
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        if i < 0:
            return
        if type(self.nums[i]) != int:
            return
        if i != j:
            self.sum += self.sumRange(i, j - 1) + self.nums[j]
            return self.sum
        else:
            return self.nums[i]

test = NumArray()
sumres = test.sumRange(0,1)
print sumres

