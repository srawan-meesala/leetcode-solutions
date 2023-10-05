import random

class RandomizedSet:


    def __init__(self):
        self.ans = {}

    def insert(self, val: int) -> bool:
        if val not in self.ans.keys():
            self.ans.__setitem__(val, val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.ans.keys():
            return False
        else:
            del self.ans[val]
            return True

    def getRandom(self) -> int:
        li = list(self.ans.values())
        return random.choice(li)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()