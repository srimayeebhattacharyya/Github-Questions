class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l=[]
        for start in range(1,9):
            num=start
            for next_digit in range(start+1,10):
                num=num*10+next_digit
                if low<=num<=high:
                    l.append(num)
        return sorted(l)