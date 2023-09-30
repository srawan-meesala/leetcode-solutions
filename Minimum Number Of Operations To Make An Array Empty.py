from collections import Counter

class Solution:
    def minOperations(self, nums) -> int:
        x = Counter(nums)
        ans = 0
        for i in x.keys():
            if x[i]==1:
                return -1
            else:
                while x[i]>0:
                    if x[i]==3 or x[i]>4:
                        x[i] -=3
                        ans+=1
                    else:
                        x[i] -= 2
                        ans+=1
        return ans
                