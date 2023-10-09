class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine)<len(ransomNote):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] in d1.keys():
                d1[ransomNote[i]] += 1
            else:
                d1.__setitem__(ransomNote[i],1)
        for i in range(len(magazine)):
            if magazine[i] in d2.keys():
                d2[magazine[i]] += 1
            else:
                d2.__setitem__(magazine[i],1)
        for i in d1.keys():
            if i not in d2.keys() or d2[i]<d1[i]:
                return False
        return True