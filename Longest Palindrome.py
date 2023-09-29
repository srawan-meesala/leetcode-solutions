class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        count = 0
        if len(s) == 1:
            return 1
        else:
            k = {}
            for i in s:
                if i in k:
                    k[i]+=1
                else:
                    k.__setitem__(i, 1)
            for l in k:
                if k[l]>=2:
                    if k[l]%2==0:
                        count+=k[l]
                        k[l] = 0
                    else:
                        count+=k[l]-1
                        k[l] = 1
            if n-count > 0:
                return count+1
            else:
                return count
