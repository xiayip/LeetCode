class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        # start from 0
        def kth(num1, num2, k, s1, e1, s2, e2):
            if s1 >= e1:
                return num2[s2 + k]
            if s2 >= e2:
                return num1[s1 + k]
            if k == 0:
                return min(num1[s1], num2[s2])

            m = (e1 + s1) / 2
            n = (e2 + s2) / 2

            if (m - s1) + (n - s2) < k:
                if num1[m] < num2[n]:
                    return kth(num1, num2, k - (m - s1) - 1, m + 1, e1, s2, e2)
                else:
                    return kth(num1, num2, k - (n - s2) - 1, s1, e1, n + 1, e2)
            else:  # m+n >= k, m+n cover k+1 element so we can reduce larger half
                if num1[m] < num2[n]:
                    return kth(num1, num2, k, s1, e1, s2, n)
                else:
                    return kth(num1, num2, k, s1, m, s2, e2)

        m = len(num1)
        n = len(num2)
        length = m + n
        if length % 2 == 0:
            return (kth(num1, num2, length / 2 - 1, 0, m, 0, n) + kth(num1, num2, length / 2, 0, m, 0, n)) / 2.0
        return kth(num1, num2, length / 2, 0, m, 0, n)






    # def findMedian(self,nums):
    #     m = len(nums)/2
    #
    #     return
    #
    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     len1 = len(nums1)
    #     len2 = len(nums2)
    #     len_a = len1 + len2
    #     res = 0
    #     if len1 == 0:
    #         if (len_a) % 2 == 0:
    #             res = (nums2[len2/2]+nums2[len2/2-1])/2.0
    #         else:
    #             res = nums2[len(nums2)/2]
    #         return res
    #     elif len2 == 0:
    #         if (len_a) % 2 == 0:
    #             res = (nums1[len1/2]+nums1[len1/2-1])/2.0
    #         else:
    #             res = nums1[len(nums1)/2]
    #         return res
    #     m1 = nums1[len1/2]
    #     m2 = nums2[len2/2]
    #     if (len_a) % 2 == 0:
    #         flag = "even"
    #     else:
    #         flag = "odd"
    #     if nums1[-1] < nums2[0]: # just append
    #         nums1.extend(nums2)
    #         mid = len_a / 2
    #         if flag == "even":
    #             res = (nums1[mid] + nums1[mid-1]) / 2.0
    #         else:
    #             res = nums1[mid]
    #     elif nums2[-1] < nums1[0]:
    #         nums2.extend(nums1)
    #         mid = len_a / 2
    #         if flag == "even":
    #             res = (nums2[mid]+nums2[mid-1]) / 2.0
    #         else:
    #             res = nums2[mid]
    #     else:
    #         if m1 < m2:
    #             while m1 < m2:
    #                 nums1 = nums1[len(nums1) / 2:]
    #                 nums2 = nums2[:len(nums2) / 2+1]
    #                 if nums1:
    #                     temp1 = nums1[len(nums1) / 2]
    #                     if temp1 < m2:
    #                         m1 = temp1
    #                     else:
    #                         break
    #                 if nums2:
    #                     temp2 = nums2[len(nums2) / 2]
    #                     if m1 < temp2:
    #                         m2 = temp2
    #                     else:
    #                         break
    #         if m1 > m2:
    #             while m1 > m2:
    #                 nums1 = nums1[:len(nums1) / 2+1]
    #                 nums2 = nums2[len(nums2) / 2:]
    #                 if nums1:
    #                     temp1 = nums1[len(nums1) / 2]
    #                     if temp1 > m2:
    #                         m1 = temp1
    #                     else:
    #                         break
    #                 if nums2:
    #                     temp2 = nums2[len(nums2) / 2]
    #                     if m1 > temp2:
    #                         m2 = temp2
    #                     else:
    #                         break
    #
    #         if flag == "even":
    #             res = (m1 + m2) / 2.0
    #         else:
    #             res = m1
    #
    #         # while len(nums1)>3 or len(nums2)>3:
    #         #     if m1 < m2:
    #         #         nums1 = nums1[len(nums1) / 2 - 1:]
    #         #         nums2 = nums2[:len(nums2) / 2 + 1]
    #         #         m1 = nums1[len(nums1) / 2]
    #         #         m2 = nums2[len(nums2) / 2]
    #         #     elif m1 > m2:
    #         #         nums1 = nums1[:len(nums1) / 2 + 1]
    #         #         nums2 = nums2[len(nums2) / 2 - 1:]
    #         #         m1 = nums1[len(nums1) / 2]
    #         #         m2 = nums2[len(nums2) / 2]
    #         #     else:
    #         #         nums1 = nums1[len(nums1) / 2-1:len(nums1) / 2+1]
    #         #         nums2 = nums2[len(nums2) / 2-1:len(nums2) / 2+1]
    #         # nums1.extend(nums2)
    #         # nums1.sort()
    #         # mid = len(nums1) / 2
    #         # if flag == "even":
    #         #     res = (nums1[mid] + nums1[mid-1]) / 2.0
    #         # else:
    #         #     res = nums1[mid]
    #     return res

test = Solution()
print test.findMedianSortedArrays([1, 3, 4, 6, 7, 8, 10],[2, 5, 9, 11, 13])
# print test.findMedianSortedArrays([1,2],[3,4])

