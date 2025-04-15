class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charToCount = Counter(s)
        output = []
        prepend = []
        orderSet = set(list(order))
        
        for char in order:
            if char in charToCount:
                output += charToCount[char] * char
        
        for char in s:
            if char not in orderSet:
                prepend += char
        
        output += prepend
        
        return "".join(output)
        