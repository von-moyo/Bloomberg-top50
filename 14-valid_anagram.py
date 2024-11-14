def is_anagram(s: str, t: str) -> bool:
    # Edge case: if the lengths differ, they can't be anagrams
    if len(s) != len(t):
        return False

    # Create a hash map (dictionary) to count characters
    count_map = {}

    # Count each character in `s`
    for char in s:
        if char in count_map:
            count_map[char] += 1
        else:
            count_map[char] = 1

    # Subtract count for each character in `t`
    for char in t:
        if char in count_map:
            count_map[char] -= 1
            # If count goes negative, `t` has extra characters
            if count_map[char] < 0:
                return False
        else:
            # Character not in `s`, so `s` and `t` are not anagrams
            return False

    # Check if all counts are zero
    for value in count_map.values():
        if value != 0:
            return False

    return True


# Time Complexity: 
# O(n), where n is the length of s or t (they must be the same length to be anagrams).
# Space Complexity: 
# O(1) if assuming fixed character set size (like 26 lowercase letters) or O(k) if the number of unique characters is variable.