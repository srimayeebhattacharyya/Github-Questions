class Solution:
    def reverseParentheses(self, s: str) -> str:
        i = 0
        res = [[]]

        while i < len(s):
            if s[i] == "(":
                res.append([])
                i += 1

            elif s[i] == ")":
                ans = res.pop()
                ans.reverse()
                res[-1].extend(ans)
                i += 1

            else:
                res[-1].append(s[i])
                i += 1

        return "".join(res[0])