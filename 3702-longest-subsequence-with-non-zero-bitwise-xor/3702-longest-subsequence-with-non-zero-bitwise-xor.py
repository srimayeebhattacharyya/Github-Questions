class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        tot=0
        for x in nums:
            tot^=x
        if tot!=0:
            return len(nums)
        if all(x==0 for x in nums):
            return 0
        return len(nums)-1