# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        first = dummy
        second = dummy
        # Advances first pointer so the gap between first and second is n nodes apart
        # n+1 bc We position the second pointer one node before the node we want to delete
        for i in range(n+1):
            first = first.next
        
        #While the first pointer not null, move both ptrs to maintain the gap
        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next