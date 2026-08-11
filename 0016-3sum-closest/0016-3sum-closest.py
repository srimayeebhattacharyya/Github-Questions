class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum=float('inf')
        for i in range(len(nums)-2):
            #skip duplicates
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1#to skip duplicates
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==target :
                    return sum
                    #To skip duplicates
                if abs(sum-target)<abs(closest_sum-target):
                    closest_sum=sum
                if sum<target:
                    left+=1
                else:
                    right-=1
        return closest_sum