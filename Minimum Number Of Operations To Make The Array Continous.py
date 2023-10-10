import bisect

class Solution:
    def minOperations(self, nums) -> int:
        n = len(nums)
        s = sorted(set(nums))
        ans = n
        for i, start in enumerate(s):
            end = start+n-1
            k = bisect.bisect_right(s, end)
            num_uniques = k-i
            ans = min(ans, n-num_uniques)
        return ans