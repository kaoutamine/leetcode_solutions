class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        #lesson learned here : use a set and not an array for the vowels!!!!!
        #also I didn't know python will iterate through each char since its
        #an array damn
        p1, p2 = 0, k
        
        n = len(s)
        max_num = sum([1 for c in s[:k] if c in vowels])
        num_vowels = max_num
        for p2 in range(k, n):
            if s[p1] in vowels:
                num_vowels -= 1
            p1 += 1
            if s[p2] in vowels:
                num_vowels +=1
            max_num = max(num_vowels, max_num)

        return max_num
            

        