import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # Max-heap (priority, taskId) but stored as (-priority, -taskId, taskId)
        self.heap = []
        
        # Dictionaries to store current tasks
        self.taskUser = {}   # taskId -> userId
        self.taskPri = {}    # taskId -> priority

        # Add initial tasks
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # Store mappings
        self.taskUser[taskId] = userId
        self.taskPri[taskId] = priority
        
        # Push into heap (negative values = max-heap behavior)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.taskPri:
            # Update in map
            self.taskPri[taskId] = newPriority
            # Push new priority into heap
            heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskPri:
            # Remove from dictionaries (heap is lazily cleaned later)
            del self.taskPri[taskId]
            del self.taskUser[taskId]

    def execTop(self) -> int:
        # Pop until we find a valid task
        while self.heap:
            negPri, negTaskId, taskId = heapq.heappop(self.heap)
            # Check if task is still valid
            if taskId in self.taskPri and self.taskPri[taskId] == -negPri:
                userId = self.taskUser[taskId]
                # Remove executed task
                del self.taskPri[taskId]
                del self.taskUser[taskId]
                return userId
        return -1

        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()