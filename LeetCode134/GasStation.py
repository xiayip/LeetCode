class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        left = 0
        start_p = []
        n = len(gas)
        if n == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1

        for i in range(len(gas)):
            if left < gas[i]-cost[i]:
                left = gas[i] - cost[i]
                start_p = []
                start_p.append(i)
            elif left == gas[i]-cost[i]:
                start_p.append(i)
        print start_p

        for start in start_p:
            k = start
            tank = [0 for _ in range(n)]
            while k != start-1:
                if k == n-1:
                    k = -1
                tank[k+1] = tank[k] + gas[k] - cost[k]
                if tank[k+1] < 0:
                    break
                else:
                    k = k + 1
            print tank
        if tank[k] + gas[k] - cost[k] < 0:
            return -1
        return start_p


test = Solution()
print test.canCompleteCircuit([6,1,4,3,5],[3,8,2,4,2])
