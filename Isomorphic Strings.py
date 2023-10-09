class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if n==1:
            return True
        d1 = {}
        for i in range(n):

            if s[i] in d1.keys():
                if d1[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in d1.values():
                    return False
                d1.__setitem__(s[i],t[i])

        return True
