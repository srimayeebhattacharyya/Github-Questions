class Solution:
    def sumGame(self, nums: str) -> bool:
        n=len(nums)
        half=n//2
        s1=s2=c1=c2=0
        for i in nums[:half]:
            if i=="?":
                c1+=1
            else:
                s1+=int(i)
        for i in nums[half:]:
            if i=="?":
                c2+=1
            else:
                s2+=int(i)
        total=c1+c2
        if total%2==1:
            return True
        return  2 * (s1 - s2) != 9 * (c2 - c1)