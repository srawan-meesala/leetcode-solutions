class Solution:
    def countPoints(self, rings: str) -> int:
        d = {}
        for i in range(0,len(rings)-1,2):
            if rings[i+1] in d.keys():
                d[rings[i+1]].add(rings[i])
            else:
                d.__setitem__(rings[i+1],set(rings[i]))
        ans = 0
        for i in d.values():
            if len(i)==3:
                ans+=1
        return ans