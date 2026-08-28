class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1

        odds = [i for i, x in enumerate(count) if x % 2]
        if len(odds) > 1:
            return ""

        middle = chr(odds[0] + 97) if odds else ""
        count = [x // 2 for x in count]
        t = target[:len(s) // 2]

        def build(left):
            return left + middle + left[::-1]

        # Match target's left half as far as possible.
        left, remaining = [], count[:]
        for ch in t:
            c = ord(ch) - 97
            if not remaining[c]:
                break
            left.append(ch)
            remaining[c] -= 1
        else:
            candidate = build("".join(left))
            if candidate > target:
                return candidate

        # Increase the rightmost possible position.
        while True:
            i = len(left)

            if i < len(t):
                current = ord(t[i]) - 97
                for c in range(current + 1, 26):
                    if remaining[c]:
                        remaining[c] -= 1
                        left.append(chr(c + 97))
                        left.extend(
                            chr(c + 97) * remaining[c]
                            for c in range(26)
                        )
                        return build("".join(left))

            if not left:
                return ""

            remaining[ord(left.pop()) - 97] += 1