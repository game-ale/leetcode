class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp  = []
        for char in s:
            if char.isalnum():
                temp.append(char.lower())
        return temp == temp[::-1]
        