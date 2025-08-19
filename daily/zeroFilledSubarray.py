from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                if count > 0:
                    total += count * (count + 1) // 2
                    count = 0
        # handle case where array ends with zeros
        if count > 0:
            total += count * (count + 1) // 2
        return total



#--------2nd solution 

from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                total += count
            else:
                count = 0
        return total
