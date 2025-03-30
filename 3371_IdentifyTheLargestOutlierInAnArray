class Solution:
    """this problem is super confusing and intimidating. First let's try
    to find the brute force solution somehow : """ 
    def getLargestOutlier(self, nums: List[int]) -> int:
        biggest = - inf
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                total = 0
                for k, num3 in enumerate(nums):
                    if k != i and k != j:
                        total += num3
                if total == num1 and biggest < num2:
                    biggest = num2
                if total == num2 and biggest < num1:
                    biggest = num1 
        return biggest

"""Yeap, the brute force solution clearly does not work so where can I improve it"""


""" I have improved the worst case solution by gettingrid of the third loop
by remembering the total and also I I have improved the conditiion on biggest"""
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        biggest = -inf
        total = sum(nums)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                num1 = nums[i]
                num2 = nums[j]
                specialTotal = total - num1 - num2
                if specialTotal == num1 and num2 > biggest:
                    biggest = num2
                if specialTotal == num2 and num1 > biggest:
                    biggest = num1
        return biggest


"""I'm a fucking twat, it's an arithmetic equation that should be solved
It then becomes linear time because I'm looking at each element"""

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        count = Counter(nums)
        max_outlier = None

        for num in nums:
            # Assume num is num1 and look for matching num2
            num2 = total - 2 * num
            if num2 in count:
                if num2 == num and count[num] < 2:
                    continue  # can't pair the number with itself unless it appears twice
                candidate = max(num, num2)
                if max_outlier is None or candidate > max_outlier:
                    max_outlier = candidate

        return max_outlier if max_outlier is not None else -1


        