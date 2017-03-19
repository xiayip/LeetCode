class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.re_sort(nums,0)

    def re_sort(self, num_s, n):
        if num_s[n] == num_s[num_s[n]-1]:
            print num_s[n]
        else:
            j = num_s[n] - 1
            num_s[n], num_s[j] = num_s[j], num_s[n]
            self.re_sort(num_s, n)



test = Solution()
print test.findDuplicates([4,3,2,7,8,2,3,1])