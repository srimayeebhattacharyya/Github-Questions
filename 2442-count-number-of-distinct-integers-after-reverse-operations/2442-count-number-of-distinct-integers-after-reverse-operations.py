class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        m=[]
        digit=[str(i)[::-1] for i in nums]
        # print(digit)
        for j in range(len(digit)):
            if digit[j][0]=='0':
                digit[j]=digit[j][1:]
        for k in range(len(digit)):
            digit[k] = int(digit[k])
        m=nums+digit
        # print(m)
        return len(set(m))