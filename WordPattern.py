class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        t = s.split(' ')
        n = len(pattern)

        if len(t) != n:
            return False

        d1 = {}
        for i in range(n):

            if pattern[i] in d1.keys():
                if d1[pattern[i]]!=t[i]:
                    return False
            else:
                if t[i] in d1.values():
                    return False
                d1.__setitem__(pattern[i],t[i])

        return True