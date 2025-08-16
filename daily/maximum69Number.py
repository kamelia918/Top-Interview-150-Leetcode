class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))  #replaces only the first occurrence of "6" with "9"
