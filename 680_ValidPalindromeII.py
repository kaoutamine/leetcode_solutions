class Solution:
    def checkPalindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False, i, j
            i += 1
            j -= 1
        return True, i, j
        

    def validPalindrome(self, s: str) -> bool:
        validity, i, j = self.checkPalindrome(0, len(s) - 1, s)
        if validity == True:
            return True

        validity, _, _ = self.checkPalindrome(i + 1, j, s)
        if validity == True:
            return True
        validity, _, _ = self.checkPalindrome(i, j - 1, s)
        
        return validity


        
                
                



        