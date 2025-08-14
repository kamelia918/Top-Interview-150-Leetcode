class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good=""
        count = 1
        for i in range(1, len(num)):
            if(num[i-1]==num[i]):
                count +=1
                if(count==3):
                    if (num[i]>good):
                        good=num[i]
            else:
                count=1
        return good*3


        