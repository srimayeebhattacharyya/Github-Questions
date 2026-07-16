import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = nums[0]
        p = []

        for i in range(len(nums)):
            mx = max(mx, nums[i])    
            n = math.gcd(nums[i], mx)
            p.append(n)

        p.sort()

        ans = 0
        left = 0
        right = len(p) - 1

        while left < right:
            ans += math.gcd(p[left], p[right])
            left += 1
            right -= 1

        return ans