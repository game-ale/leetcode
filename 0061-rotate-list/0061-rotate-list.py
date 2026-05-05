# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        tail.next = head

        k = k % n

        steps = n - k - 1
        newTail = head

        while steps > 0:
            newTail = newTail.next
            steps -= 1

        newHead = newTail.next

        newTail.next = None

        return newHead