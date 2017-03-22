class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if head.next == None:
                return head
            f = head.next
            first_node = head
            sec_node = head.next
            while sec_node != None: # if node num is odd
                # swap
                first_node.next = sec_node.next
                sec_node.next = first_node
                if first_node.next == None: # if it is the last node
                    break
                else:
                    if first_node.next.next != None:
                        temp_node = first_node.next
                        first_node.next = first_node.next.next
                    else:
                        break
                first_node = temp_node
                sec_node = temp_node.next
            return f
        else:
            return []


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node.next = node2
node2.next = node3
node3.next = node4
test = Solution()
h = test.swapPairs([])
print h