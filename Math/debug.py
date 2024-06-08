def is_graphical_erdos_gallai(degree_sequence):
    # Sort the degree sequence in non-increasing order
    degree_sequence.sort(reverse=True)
    n = len(degree_sequence)
    # Check if the sum of the degree sequence is even
    if sum(degree_sequence) % 2 != 0:
        return False

    # Apply the Erdős-Gallai condition
    for k in range(1, n + 1):
        left_side = sum(degree_sequence[:k])
        right_side = k * (k - 1) + sum(min(d, k) for d in degree_sequence[k:])
        print(left_side, right_side)
        if left_side > right_side:
            return False

    return True

# Test the function with the given degree sequence
degree_sequence = [7, 7, 5, 5, 5, 3, 2, 2]
is_graphical = is_graphical_erdos_gallai(degree_sequence)
print(f"The degree sequence {degree_sequence} is graphical: {is_graphical}")