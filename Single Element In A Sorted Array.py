class Solution:

    def binarysearch(self, left, right, nums):
        while left<right:
            mid = (left+right)//2
            if mid%2==0:
                isEven = True  
            else:
                isEven = False
            if nums[mid]==nums[mid+1]:
                if isEven:
                    return self.binarysearch(mid+2, right, nums)
                else:
                    return self.binarysearch(left, mid-1, nums)
            elif nums[mid]==nums[mid-1]:
                if isEven:
                    return self.binarysearch(left, mid-2, nums)
                else:
                    return self.binarysearch(mid+1, right, nums)
            else:
                return mid
        return left

    def singleNonDuplicate(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        return nums[self.binarysearch(0, len(nums)-1, nums)]