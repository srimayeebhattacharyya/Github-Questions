class Solution:
    def maxSumOfSquares(self, num: int, sum1: int) -> str:
        # If the sum cannot be formed with num digits (max possible is 9 * num)
        if sum1 <= 0 or sum1 > 9 * num:
            return ""

        # Greedily take as many 9s as possible
        nines = sum1 // 9
        rem = sum1 % 9

        digits = [9] * nines
        if rem > 0:
            digits.append(rem)

        # Pad with zeros to match length 'num'
        digits += [0] * (num - len(digits))

        # Sort descending to get the largest possible number
        digits.sort(reverse=True)

        return "".join(map(str, digits))