def two_sorted_arrays_sum_to_target(arr1, arr2, target):
    # Ensure arr1 is the smaller array for efficiency
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    # Perform binary search over both arrays
    low, high = 0, len(arr1) - 1
    while low <= high:
        mid = (low + high) // 2
        complement = target - arr1[mid]
        
        # Binary search for complement in the second array
        left, right = 0, len(arr2) - 1
        while left <= right:
            mid2 = (left + right) // 2
            if arr2[mid2] == complement:
                return True
            elif arr2[mid2] < complement:
                left = mid2 + 1
            else:
                right = mid2 - 1
        
        # Adjust search range in the first array
        if arr1[mid] < complement:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Time: O(logm+logn), which simplifies to O(logn) if m≈n.
# space: O(1)