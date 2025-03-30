

"""Brute force method where I iterate through every element and go look to the right if it's 
a subarray that respects the product condition. Unfortunately, this won't work because it's 
O(n**2) complexity """
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            product = nums[i]
            if product >= k:
                continue
            else:
                res += 1
            
            j = i + 1
            while j < len(nums):
                product = product * nums[j]
                if product < k:
                    res += 1
                    j += 1
                else:
                    break

        return res
            

"""how many subarrays are there in between my two pointers?
        If I manage to go from 0 to 2, there's 10, 5 and [10, 5] so 3
        If I go from 0 to 3 , there's 6 of them 
        the trick is to count the arrays ending at the current right index 
        because we then know there's right - left + 1 of them"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k <= 1:
            return 0
        res = 0
        left, right = 0, 0
        product = 1

        for right in range(len(nums)):
            product = product * nums[right]
            while product >= k and left < right:
                product = product / nums[left]
                left += 1

            if product < k:
                res += right - left + 1
                continue

        return res
            
            



        

        