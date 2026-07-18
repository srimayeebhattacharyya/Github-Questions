class Solution:
    def findGCD(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l=min(nums)
        m=max(nums)
        while m:
            l,m=m,l%m        
        return l