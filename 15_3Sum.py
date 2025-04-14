from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        output.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        #ahhh it was so annoying to get rid of the duplicates!!!!
        #sorting the sublist and then adding it to a set was the only way
        #using the hashing of an ordered tuple to efficiently prevent       duplicates....
        return list(output)



        