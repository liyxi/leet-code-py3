# pass in 68 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        z = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            z += x + y
            r = z // 10
            p.next = ListNode(z-r*10)
            p = p.next
            z = r
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
        if r != 0:
            p.next = ListNode(r)
        return head.next
        
