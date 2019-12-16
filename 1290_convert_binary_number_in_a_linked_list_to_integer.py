# pass in 20 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            head = head.next
            result = result << 1
            result += head.val
        return result
