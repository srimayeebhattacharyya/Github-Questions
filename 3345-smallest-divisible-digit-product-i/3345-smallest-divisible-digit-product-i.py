class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        s=0
        for i in range(n,n+10):
            digit_product = math.prod(int(d) for d in str(i))
            if digit_product%t==0:
                return i