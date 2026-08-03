class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        h = {}
        for ch in s:
            h[ch] = h.get(ch, 0) + 1

        for ch in h:
            if h[ch] < k:
                ans = 0
                for part in s.split(ch):
                    ans = max(ans, self.longestSubstring(part, k))
                return ans

        return len(s)