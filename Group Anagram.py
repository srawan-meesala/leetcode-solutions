from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        if len(strs)==0:
            return [[]]
        d = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in d.keys():
                d[s].append(i)
            else:
                d.__setitem__(s,[i])
        return list(d.values())