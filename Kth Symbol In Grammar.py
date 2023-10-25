class Solution:
    def kthGrammar(self, n: int, k: int):
        def score(n,k):
            if n==1:
                return '0'
            else:
                if score(n-1, (k+1)//2)=='0':
                    return '1' if k%2==0 else '0'
                else:
                    return '0' if k%2==0 else '1'
        return int(score(n,k))