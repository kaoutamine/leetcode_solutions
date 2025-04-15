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



        #smooth solution with ordering, dual pointers and ignoring duplicates :

        from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        n = len(nums)
        for i in range(0, n - 2):
            #skip potential duplicates on i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1 
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    #we have appended and now need to skip the duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
                
        return output

                #now we need to skip the duplicates
                
                
                    




        
        
