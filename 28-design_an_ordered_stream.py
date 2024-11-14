class OrderedStream:
    def __init__(self, n: int):
        self.pointer = 1
        self.seen = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.seen[idKey] = value
        
        res = []
        
        while self.pointer in self.seen:
            res.append(self.seen[self.pointer])
            del self.seen[self.pointer]
            self.pointer += 1
        
        return res
    
# Time Complexity = O(n)
# Space Complexity = O(n)