class Solution:
    def sumAndMultiply(self, n: int) -> int:
        l=[]
        m=[]
        for i in str(n):
            if i!='0':
                l.append(int(i))
                m.append(i)
        if not m: return 0
        n=sum(l)
        p = int(''.join(m))
        return p*n