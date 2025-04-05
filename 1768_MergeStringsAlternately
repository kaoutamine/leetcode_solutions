class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        l1, l2 = len(word1), len(word2)
        i = 0

        while i < min(l1, l2):
            output += word1[i]
            output += word2[i]
            i += 1
        while i < l1:
            output += word1[i]
            i += 1
        while i < l2:
            output += word2[i]
            i += 1

        return output

        
        