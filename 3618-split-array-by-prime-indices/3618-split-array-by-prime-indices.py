class Solution:
    def isPrime(self,val):
        if val<2: return False
        for i in range(2,int(math.sqrt(val)+1)):
            if val%i==0:
                return False
        return True
    def splitArray(self, nums: List[int]) -> int:
        arrA=[]
        arrB=[]
        for i in range(len(nums)):
            if self.isPrime(i):
                arrA.append(nums[i])
            else:
                arrB.append(nums[i])
        return abs(sum(arrA)-sum(arrB))