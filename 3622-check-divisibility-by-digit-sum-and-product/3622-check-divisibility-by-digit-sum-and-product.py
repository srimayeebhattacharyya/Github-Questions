from functools import reduce
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        d=[int(d) for d in str(n)]
        if len(d)==1:
            return False
        digit=sum(d)
        m=reduce(lambda x, y: x * y, d)
        return n%(digit+m)==0