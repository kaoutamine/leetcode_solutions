"""The idea is that you want to store in a stack (classic parenthesis problem) the upcoming (
parentheses. When you encounter a parenthesis that should not be there, you should store it 
into a set such that once you've done one entire pass, you can efficiently check 
in the string if this specific parenthesis should be removed. If you don't store it into
a set you run into the issue that checking if the index is in the list of unwanted indexes
you get a runtime of O(n) which makes your second pass O(n**2)"""



class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p_stack = []
        unwanted_indexes = set()
        for i, char in enumerate(s):
            if char == "(":
                p_stack.append(i)
            elif char == ")":
                if len(p_stack) == 0:
                    #that index should be removed
                    unwanted_indexes.add(i)
                else:
                    p_stack.pop()
            else:
                continue
        
        while len(p_stack) > 0:
            unwanted_indexes.add(p_stack.pop())
        
        output = ""
        for i, char in enumerate(s):
            if i not in unwanted_indexes:
                output += char
        return output




                
            
        