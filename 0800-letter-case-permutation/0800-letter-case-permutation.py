class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        
        def backtrack(index, path):
            if index == len(s):
                ans.append("".join(path))
                return
            if s[index].isdigit():
                backtrack(index + 1, path + [s[index]])
            else:
                backtrack(index + 1, path + [s[index].lower()])
                backtrack(index + 1, path + [s[index].upper()])
        
        backtrack(0, [])
        return ans