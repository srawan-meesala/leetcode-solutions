from collections import Counter

class Solution:
    def majorityElement(self, nums) -> int:
        return Counter(nums).most_common(1)[0][0]