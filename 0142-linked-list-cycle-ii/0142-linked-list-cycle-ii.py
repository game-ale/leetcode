# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point = head
        visited = set()
        while point:
            if point in visited:
                return point
            visited.add(point)
            point = point.next
        return None
