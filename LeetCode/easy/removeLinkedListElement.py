# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # Dummy node to handle edge cases easily
        prev = dummy
        cur = head
        
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            # shift curr
            cur = cur.next
        return dummy.next