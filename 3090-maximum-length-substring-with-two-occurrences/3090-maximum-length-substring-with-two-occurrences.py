class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m = {}

        i = 0
        res = 0

        for j in range(len(s)):
            m[s[j]] = m.get(s[j], 0) + 1

            while m[s[j]] > 2:
                m[s[i]] -= 1
                i += 1

            res = max(res, j - i + 1)

        return res