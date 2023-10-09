class Solution:

    def binary(self, nums, target, left, right):
        if left>right:
            return -1
        n = (left+right)//2
        if target==nums[n]:
            return n
        elif target>nums[n]:
            return self.binary(nums, target, n+1, right)
        else:
            return self.binary(nums, target, left, n-1)

    def searchRange(self, nums, target: int):
        if len(nums)==1:
            if nums[0]==target:
                return [0, 0]
            else:
                return [-1, -1]
        k = self.binary(nums, target, 0, len(nums)-1)
        ans = [k, k]
        if k==-1:
            return [-1, -1]
        else:
            while ans[0]>0 and nums[ans[0]-1]==target:
                ans[0]-=1
            while ans[1]<len(nums)-1 and nums[ans[1]+1]==target:
                ans[1]+=1
            return ans