class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target >= nums[i - 1] and target <= nums[i] and i > 0:
                return i
        if nums[0] >= target:
            return 0
        else:
            return len(nums)