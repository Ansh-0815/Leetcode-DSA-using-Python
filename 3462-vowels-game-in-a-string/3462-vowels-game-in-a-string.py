class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels=set("aeiou")
        for i in s:
            if i in vowels:
                return True
        else:
            return False