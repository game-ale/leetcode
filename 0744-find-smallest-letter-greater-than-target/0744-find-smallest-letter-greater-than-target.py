class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        n,k  = len(letters)-1,len(letters)
        while n>=0 and ord(letters[n])>ord(target):
            n-=1
        return (letters[(n+1)%k])

        