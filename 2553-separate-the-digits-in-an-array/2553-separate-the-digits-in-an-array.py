class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res=[]
        for num in nums:
            m=str(num)
            for ch in m:
                res.append(int(ch))
        return res