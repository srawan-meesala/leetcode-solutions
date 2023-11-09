class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = (10**9)+7
        x,y = 0,0
        ans = 0
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                y = i+1
            else:
                ans += ((y-x+1)*(y-x+2)//2) % MOD
                x = i+1
                y = x
        ans += ((y-x+1)*(y-x+2)//2) % MOD
        return ans % MOD