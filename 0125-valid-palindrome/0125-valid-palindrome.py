class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i, char in enumerate(s):
            if char.isalnum():
                t+=char.lower()
        for j in range(len(t)):
            if t[j] != t[-1 - j]:
                return False
        return True
        

            




        