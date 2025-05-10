class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        return -1 if (K:=(sum(nums1), nums1.count(0), sum(nums2), nums2.count(0))) and ((K[1]==0 and K[0]<K[2]+K[3]) or (K[3]==0 and K[2]<K[0]+K[1])) else max(K[0]+K[1], K[2]+K[3])