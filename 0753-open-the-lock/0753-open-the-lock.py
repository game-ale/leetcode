class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        forward = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }
        backward = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }
        que = deque()
        ans = 0
        visited = set(deadends)
        if "0000" in visited:
            return -1
        que.append("0000")
        visited.add("0000")
        while que:
            len_que = len(que)
            for wheel in range(len_que):
                cur = que.popleft()
                if cur==target:
                    return ans
                for change in range(4):
                    new_change = list(cur)
                    new_change[change] = forward[new_change[change]]
                    new_change = "".join(new_change)
                    if new_change not in visited:
                        que.append(new_change)
                        visited.add(new_change)
                    new_change = list(cur)
                    new_change[change] = backward[new_change[change]]
                    new_change = "".join(new_change)
                    if new_change not in visited:
                        que.append(new_change)
                        visited.add(new_change)
            ans+=1
        return -1

