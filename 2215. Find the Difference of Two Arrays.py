class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        missing1, missing2 = [], []
        for num1 in s1:
            if num1 not in s2:
                missing1.append(num1)
        
        for num2 in s2:
            if num2 not in s1:
                missing2.append(num2)

        return [missing1, missing2]



        