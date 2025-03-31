class Solution:
    def canJump(self, nums: List[int]) -> bool:
        GOOD, BAD = 0, 1
        hashmap = {}
        n = len(nums)
        hashmap[n - 1] = GOOD

        for i in range(n - 2, -1, -1):
            max_range = min(n - 1, i + nums[i])
            j = i + 1

            while j <= max_range: 
                if hashmap[j] == GOOD:
                    hashmap[i] = GOOD
                    break
                j += 1
            if i not in hashmap:
                hashmap[i] = BAD
        
        if hashmap[0] == BAD:
            return False
        else:
            return True
            
                
        