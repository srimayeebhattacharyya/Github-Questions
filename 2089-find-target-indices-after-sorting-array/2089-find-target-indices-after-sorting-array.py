class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        a=[]
        s=0
        for i in range(len(nums)):
            if target in nums:
                if nums[i] == target:
                    a.append(i)
            else:
                return []
        return a