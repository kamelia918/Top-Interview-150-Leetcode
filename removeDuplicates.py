
from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:   
        num = nums[0]
        index = 1
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] != num:
                num = nums[i]
                nums[index] = num
                index += 1
                count = 1
            else:
                if count < 2:
                    nums[index] = num
                    index += 1
                    count += 1
                else:
                    count += 1
        
        return index