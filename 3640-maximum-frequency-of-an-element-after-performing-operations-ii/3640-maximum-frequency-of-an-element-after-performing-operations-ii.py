from typing import List
import bisect
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        freq = Counter(nums)
        ans = 1

        for v, already in freq.items():
            lowVal = v - k
            highVal = v + k
            L = bisect.bisect_left(nums, lowVal)
            R = bisect.bisect_right(nums, highVal)
            totalInRange = R - L
            need = totalInRange - already
            canFix = min(need, numOperations)
            ans = max(ans, already + canFix)

        l = 0
        for r in range(n):
            while l <= r and nums[r] - nums[l] > 2 * k:
                l += 1
            w = r - l + 1
            ans = max(ans, min(w, numOperations))

        return ans