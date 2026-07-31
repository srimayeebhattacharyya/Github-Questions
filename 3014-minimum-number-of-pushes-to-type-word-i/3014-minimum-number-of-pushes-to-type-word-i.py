class Solution:
    def minimumPushes(self, word: str) -> int:
        f={}
        for ch in word:
            f[ch]=f.get(ch,0)+1
        c=sorted(f.values(),reverse=True)
        ans=0
        for i,freq in enumerate(c):
            pushes=i//8+1
            ans+=pushes*freq
        return ans