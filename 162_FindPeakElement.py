class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """idea : start in the middle and binary search in a direction
        where it's known that there will be a peak. The direction is
        the one towards the higher number """ 

        n = len(nums)

        #handle edge cases
        if n == 1 or nums[0] > nums[1]:
            return 0
        #don't play with edge cases like a dumbass else you get cooked
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        hi, lo = n - 1, 0

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                lo = mid
            else:
                hi = mid
        
        
    
        