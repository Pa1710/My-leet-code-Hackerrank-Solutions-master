class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half = total // 2
        if(len(nums2) < len(nums1)):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums1) - 1
        while True:
            i = (r+l) // 2
            j = half - i - 2
            nums1_l = nums1[i] if i >= 0 else float("-infinity")
            nums1_r = nums1[i+1] if (i+1) < len(nums1) else float("infinity")
            nums2_l = nums2[j] if (j >= 0) else float("-infinity")
            nums2_r = nums2[j+1] if (j+1) < len(nums2) else float("infinity")
            if(nums1_l <= nums2_r) and (nums2_l <= nums2_r):
                if total % 2:
                    return min(nums1_r, nums2_r)
                else:
                    return (min(nums1_r, nums2_r) + max(nums1_l, nums1_l)) / 2
            if(nums1_l >= nums2_r):
                r = i-1
            else:
                l = i+1
