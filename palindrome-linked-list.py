# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # first find length
        if not head:
            return True
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        if length == 1:
            return True
        # iterate through to find begining of l2
        # remove link from l1 to l2, and mark l2
        even = False
        if length % 2 == 0:
            even = True
        cur = head
        endList = self.getEndList(cur)            
        secondList = endList.next
        
        # reverse l2 and get head
        l1 = head
        l2 = self.reverseLL(secondList)
        if l1.val != l2.val:
            return False
        # compare l1 and l2 for palindrome
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            if l1.val != l2.val:
                return False
        return True
            
        
    def reverseLL(self, head):
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
        
    def getEndList(self, cur):
        fast = cur
        slow = cur
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        
        
        
