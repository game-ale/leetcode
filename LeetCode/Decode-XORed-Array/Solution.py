class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        xor = first 
        ans = [first]
        for num in encoded:
            ans.append(num^ans[-1])
        return ans

        