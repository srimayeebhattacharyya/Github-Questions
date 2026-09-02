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
            nums2 = nums1.copy()

        elif o == len(nums1):
            nums2 = nums1.copy()

        else:
            for i in range(len(nums1)):
                if nums1[i] % 2 != 0:
                    nums2.append(nums1[i])
                else:
                    for j in range(len(nums1)):
                        if nums1[j] % 2 != 0:
                            nums2.append(nums1[i] - nums1[j])
                            break

        return True