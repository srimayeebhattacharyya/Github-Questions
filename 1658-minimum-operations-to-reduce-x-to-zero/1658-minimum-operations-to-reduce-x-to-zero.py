class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        m=sum(nums)-x
        if m<0:return -1
        s=left=0
        best=-1
        for right,num in enumerate(nums):
            s+=num
            while s>m:
                s-=nums[left]
                left+=1
            if s==m:
                best=max(best,right-left+1)
        return -1 if best<0 else len(nums)-best