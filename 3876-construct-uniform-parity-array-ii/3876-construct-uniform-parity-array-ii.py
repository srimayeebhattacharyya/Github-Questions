class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        e = o = 0
        nums2 = []

        for i in range(len(nums1)):
            if nums1[i] % 2 == 0:
                e += 1
            else:
                o += 1

        if e == len(nums1):
            return True
        if min(nums1) % 2 != 0:
            return True

        return False