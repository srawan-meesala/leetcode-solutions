class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = False
        dec = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc = True
            elif nums[i] < nums[i - 1]:
                dec = True
        if inc == True and dec == True:
            return False
        else:
            return True
