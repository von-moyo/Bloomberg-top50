def collatz_sequence(n):
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Example usage
n = 6
result = collatz_sequence(n)
print(f"Collatz sequence for {n}: {result}")

# Time Complexity:O(logn) (empirical and practical analysis).
# Space Complexity: O(logn) (to store the sequence). O(1) if we are only storing the number of iterations, not the whole sequence.



# Cache implementation
class Collatz:
    def __init__(self):
        self.cache = {}

    def collatz_length(self, n):
        # If the value is already in the cache, return it
        if n in self.cache:
            return self.cache[n]

        # Base case: sequence reaches 1
        if n == 1:
            self.cache[n] = 1
            return 1

        # Recursive computation
        if n % 2 == 0:
            next_n = n // 2
        else:
            next_n = 3 * n + 1

        # Compute the length of the sequence recursively
        length = 1 + self.collatz_length(next_n)

        # Store the result in the cache
        self.cache[n] = length

        return length

# Example usage
collatz_solver = Collatz()
n = 8
result = collatz_solver.collatz_length(n)
print(f"Collatz length for {n}: {result}")
print(collatz_solver.cache)
