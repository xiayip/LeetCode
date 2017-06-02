class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        cross = 0
        T1xrange = [A, C]
        T1yrange = [B, D]
        T2xrange = [E, G]
        T2yrange = [F, H]
        if max(T1xrange[0],T2xrange[0])<min(T1xrange[1],T2xrange[1]):
            if max(T1yrange[0],T2yrange[0])<min(T1yrange[1],T2yrange[1]):
                cross = (min(T1xrange[1],T2xrange[1])-max(T1xrange[0],T2xrange[0]))*(min(T1yrange[1],T2yrange[1])-max(T1yrange[0],T2yrange[0]))
        area = (C - A)*(D - B)+(G - E)*(H - F) - cross
        return area

test = Solution()
print test.computeArea(-3,0,3,4,0,-1,9,2)
print test.computeArea(-2,-2,2,2,-2,-2,2,2)
print test.computeArea(0,0,0,0,-1,-1,1,1)
print test.computeArea(-2,-2,2,2,3,3,4,4)
print test.computeArea(-2,-2,2,2,-3,-3,3,-1)
print test.computeArea(3,3,4,4,-2,-2,2,2)