class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        curr = float('-inf')
        ans = 0
        for x in nums:
            start, end = x - k, x + k
            pick = max(start, curr)
            if pick <= end:
                ans += 1
                curr = pick + 1
        return ans