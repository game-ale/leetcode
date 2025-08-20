# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummay = ListNode()
        ans = head
        while ans:
            next = ans.next
            ans.next = dummay.next
            dummay.next = ans
            ans = next
        return dummay.next