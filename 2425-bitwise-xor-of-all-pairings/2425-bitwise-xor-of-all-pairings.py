class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1%2==0 and len2%2==0:
            return 0
        elif len1%2==1 and len2%2==0:
            result = nums2[0]
            for num in nums2[1:]:
                result^=num
            return result
        elif len1%2==0 and len2%2==1:
            result = nums1[0]
            for num in nums1[1:]:
                result^=num
            return result
        else:
            result = nums1[0]
            for num in nums1[1:]+nums2:
                result^=num
            return result