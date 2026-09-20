class Solution:
    def reverseDegree(self, s: str) -> int:
        ind=[]
        m=["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
        for i in range(len(s)):
            ind.append((i+1)*(m.index(s[i])+1))
        return sum(ind)