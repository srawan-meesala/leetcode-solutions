from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums) -> int:
        k = Counter(nums)
        ans = 0
        for i in k.values():
            ans += i*(i-1)//2
        return ans