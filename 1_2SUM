#
class Solution:
    #brute force solution
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)

    """I thought about the non brute force with sorting. Unfortunately there are multiple issues.
    First off, because the indexes are reordered and you are asked to output indices
    It won't work without first remembering the indices of the original problem. So I need first
    to fuse the List with it's own enumerations and then order according to the value and then
    I can do the two pointer approach."""

"""Solution with two indexes and remembering the original index in python"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = [pair for pair in enumerate(nums)]
        pairs = sorted(pairs, key = lambda x : x[1])
        p1, p2 = 0, len(nums) - 1
        total = pairs[p1][1] + pairs[p2][1]

        while total != target:
            if total > target:
                p2 = p2 - 1
            else:
                p1 += 1
            total = pairs[p1][1] + pairs[p2][1]
        
        return pairs[p1][0], pairs[p2][0]
    

"""Solution with hashmap"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            search = target - num
            if search in seen:
                return i, seen[search]
            else:
                seen[num] = i