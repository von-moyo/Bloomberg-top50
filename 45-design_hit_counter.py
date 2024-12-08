# design hit counter

from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()  # Stores (timestamp, count) pairs

    def hit(self, timestamp: int) -> None:
        # If the last hit was at the same timestamp, increment the count
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1] = (timestamp, self.hits[-1][1] + 1)
        else:
            # Otherwise, add a new entry for this timestamp
            self.hits.append((timestamp, 1))

    def getHits(self, timestamp: int) -> int:
        # Remove all entries that are older than 5 minutes from the current timestamp
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.hits.popleft()
        
        # Sum up all the counts in the remaining hits to get the result
        return sum(count for _, count in self.hits)


# Time Complexities: O(1) for hit, O(n) for get_hits
# Space Complexities: O(n)