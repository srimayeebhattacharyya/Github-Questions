class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        start = 0
        comma_count = 0
        
        # Loop through power-of-1000 boundaries
        while True:
            end = min(10**(3*(comma_count+1)), n + 1) - 1
            
            # Calculate overlap with [start, end]
            if start > n:
                break
                
            overlap = max(0, min(end, n) - start + 1)
            total += overlap * comma_count
            
            start = end + 1
            comma_count += 1
            
        return total