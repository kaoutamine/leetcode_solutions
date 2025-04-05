"""Easy but I still didn't succeed at first try because I put the wrong variable name
Code is a story and I must be careful fitting every piece"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        maximum = 0
        for num in gain:
            total += num
            if maximum < total:
                maximum = total
        return maximum



        