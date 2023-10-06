class Solution:
    def integerBreak(self, n: int) -> int:
        if n<8:
            if n%2==0:
                return (n//2)**2
            else:
                return (n//2)*((n//2) + 1)
        else:
            if n%3==0:
                return 3**(n//3)
            elif n%3==1:
                return 3**(n//3 - 1) * 4
            else:
                return 3**(n//3) * 2