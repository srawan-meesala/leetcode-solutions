from collections import Counter

class Solution:
    def majorityElement(self, nums):
        n = len(nums)//3
        ans = []
        k = Counter(nums)
        for i in k.keys():
            if k[i]>n:
                ans.append(i)
        return ans