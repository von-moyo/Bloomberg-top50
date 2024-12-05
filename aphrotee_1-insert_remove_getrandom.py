# Insert, Remove, getRandom
import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict: return False

        self.arr.append(val)
        self.dict[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict: return False

        index = self.dict[val]
        lastValue = self.arr[-1]

        self.arr[index], self.dict[lastValue] = lastValue, index

        self.arr.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        randomInt = random.randint(0, len(self.arr) - 1)
        return self.arr[randomInt]