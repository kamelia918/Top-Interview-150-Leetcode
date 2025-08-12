from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        j=len(nums) - 1
        i=0
        while (i<len(nums) and j>=0 and i<=j):
            if(nums[i]!= val):
                k+=1
                i+=1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
        return k

