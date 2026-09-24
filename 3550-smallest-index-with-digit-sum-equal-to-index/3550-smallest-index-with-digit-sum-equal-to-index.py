class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digits=sum(int(char) for char in str(nums[i]))
            # print(f"Index {i}, Number {nums[i]}, Sum of digits: {digits}")
            if digits==i:
                return i
        return  -1