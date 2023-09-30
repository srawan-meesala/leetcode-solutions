class Solution:
    def minOperations(self, nums, k) -> int:
        new = [0]*k
        for i in range(len(nums)):
            if nums[i]<=k:
                new[nums[i]-1] = i
        return len(nums) - min(new)