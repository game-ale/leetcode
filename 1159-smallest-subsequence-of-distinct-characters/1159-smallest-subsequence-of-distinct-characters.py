class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1

        stack = []
        in_stack = set()

        for char in s:
            freq[char] -= 1

            if char in in_stack:
                continue

            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                removed_char = stack.pop()
                in_stack.remove(removed_char)

            stack.append(char)
            in_stack.add(char)

        return ''.join(stack)