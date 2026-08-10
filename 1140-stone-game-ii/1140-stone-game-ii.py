class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @cache
        def dp(i, m):
            if i >= n:
                return 0
            stones = 0
            res = -inf
            for x in range(1, 2 * m + 1):
                if i + x - 1 >= n:
                    break
                new_m = max(m, x)
                stones += piles[i + x - 1]
                res = max(res, stones - dp(i + x, new_m))
            return res
        diff = dp(0, 1)
        return (diff + sum(piles)) // 2