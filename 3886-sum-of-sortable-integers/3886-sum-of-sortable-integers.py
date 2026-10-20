
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(1, n + 1):
            if n % i != 0:
                continue

            result = []
            valid = True

            for j in range(0, n, i):
                subarray = nums[j:j + i]
                drops = []

                for x in range(i):
                    if subarray[x] > subarray[(x + 1) % i]:
                        drops.append(x)

                if len(drops) > 1:
                    valid = False
                    break

                if drops:
                    pos = (drops[0] + 1) % i
                    subarray = subarray[pos:] + subarray[:pos]

                result.extend(subarray)

            if valid and result == sorted(result):
                ans += i

        return ans
