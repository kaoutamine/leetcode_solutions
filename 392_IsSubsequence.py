class Solution:
    def subrec(self, posS, posT, s, t):
            if posS >= len(s):
                return True
            if posT >= len(t):
                return False
            if s[posS] == t[posT]:
                return self.subrec(posS + 1, posT + 1, s, t)
            else:
                return self.subrec(posS, posT + 1, s, t)
    
    def isSubsequence(self, s: str, t: str) -> bool:
        return self.subrec(0, 0, s, t)
        