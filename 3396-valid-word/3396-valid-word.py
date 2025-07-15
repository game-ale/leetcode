class Solution:
    def isValid(self, word: str) -> bool:
        vowel = {'a','A','e','E','i','I','o','O','u','U'}
        const = False
        vowl = False
        for c in word:
            if not c.isalnum():
                return False
            elif c.isalpha():
                if c in vowel:
                    vowl = True
                else:
                    const = True
        return (const and vowl and len(word) >= 3)
                


        