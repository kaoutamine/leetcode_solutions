class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        
        
        
        if s == goal:
            return len(set(s)) < len(s)
        
        indices = []
        
        for i in range(len(s)):
            if s[i] == goal[i]:
                continue
            indices.append(i)
            if len(indices) > 2:
                return False
            
        if len(indices) == 0 or len(indices) == 1:
            return False
            
        i1 = indices[0]
        i2 = indices[1]
        
        if s[i1] == goal[i2] and goal[i1] == s[i2]:
            return True
        else:
            return False