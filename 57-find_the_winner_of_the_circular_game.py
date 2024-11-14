class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()

        for i in range(1, n + 1):
            queue.append(i)

        while len(queue) != 1:
            for _ in range(k - 1):
                friend = queue.popleft()
                queue.append(friend)

            queue.popleft()

        return queue.pop()


# Time Complexity:
# Each time we eliminate a person, it takes O(k) operations to rotate the deque and remove the k-th person.
# This process repeats n−1 times (since we need to eliminate n - 1 people to find the winner).
# Therefore, the time complexity is O(n⋅k).

# Space Complexity:
# The deque stores all n people, so the space complexity is O(n).





