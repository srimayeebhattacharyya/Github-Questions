class Solution:
    def stoneGameVI(self, A: List[int], B: List[int]) -> int:
        m=[a+b for a,b in zip(A,B)]
        m.sort()
        L=len(A)
        d=-sum(B)+sum(m[i] for i in range(L-1,-1,-2))
        return 1 if d>0 else (-1 if d<0 else 0)