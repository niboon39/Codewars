def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged = sorted(nums1 + nums2)
    length = len(merged)
    
    if length % 2 == 0:  # If the length is even
        return (merged[(length // 2) - 1] + merged[length // 2]) / 2
    else:  # If the length is odd
        return merged[length // 2]

# Example usage
print(findMedianSortedArrays([1, 3], [2]))  # Expected output: 2.0