class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l=sorted(set(arr))
        rank = {val: i + 1 for i, val in enumerate(l)}
        r=[]
        for i in arr:
            r.append(rank[i])  
        return r