class Seg:
    def __init__(self, left=-1, right=-1):
        self.left = left
        self.right = right

    def __lt__(self, rhs):
        return (
            self.left > rhs.left
            if self.right == rhs.right
            else self.right < rhs.right
        )


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        seg = [Seg() for _ in range(26)]
        # Preprocess the left and right endpoints.
        for i in range(len(s)):
            char_idx = ord(s[i]) - ord("a")
            if seg[char_idx].left == -1:
                seg[char_idx].left = seg[char_idx].right = i
            else:
                seg[char_idx].right = i

        for i in range(26):
            if seg[i].left != -1:
                j = seg[i].left
                while j <= seg[i].right:
                    char_idx = ord(s[j]) - ord("a")
                    if (
                        seg[i].left <= seg[char_idx].left
                        and seg[char_idx].right <= seg[i].right
                    ):
                        pass
                    else:
                        seg[i].left = min(seg[i].left, seg[char_idx].left)
                        seg[i].right = max(seg[i].right, seg[char_idx].right)
                        j = seg[i].left
                    j += 1

        # Greedily select intervals.
        seg.sort()
        ans = list()
        end = -1
        for segment in seg:
            left, right = segment.left, segment.right
            if left == -1:
                continue
            if end == -1 or left > end:
                end = right
                ans.append(s[left : right + 1])

        return ans