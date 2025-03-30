class Solution:
    def handle_right(self, p1, p2, target):
        while p2 < len(target) and target[p2] == "_":
            p2 += 1 
        if p2 == len(target) or target[p2] == "L":
            return False, p2
        else:
            if p2 >= p1:
                return True, p2 + 1
            else:
                return False, p2 + 1

    def handle_left(self, p1, p2, target):
        while p2 < len(target) and target[p2] == "_":
            p2 += 1
        if p2 == len(target) or target[p2] == "R":
            return False, p2
        else:
            if p2 <= p1:
                return True, p2 + 1
            else:
                return False, p2 + 1

    def canChange(self, start: str, target: str) -> bool:
        p2 = 0
        for p1 in range(len(start)):
            if start[p1] == "_":
                continue
            if start[p1] == "R":
                valid, p2 = self.handle_right(p1, p2, target)
                if not valid:
                    return False
            else:  # start[p1] == "L"
                valid, p2 = self.handle_left(p1, p2, target)
                if not valid:
                    return False
        
        while p2 < len(target):
            if target[p2] != "_":
                return False
            p2 += 1
        
        return True
