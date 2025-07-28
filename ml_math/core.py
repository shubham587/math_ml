"""
mlmath.core - A simple machine learning math helper library.
"""

def dot_product(a, b):
    """
    Compute the dot product of two vectors.

    Args:
        a (list): First vector.
        b (list): Second vector.

    Returns:
        float: Dot product of vectors a and b.

    Example:
        >>> dot_product([1, 2, 3], [4, 5, 6])
        32
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be of same length.")
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(A, B):
    """
    Multiply two matrices using nested loops.

    Args:
        A (list of list): First matrix.
        B (list of list): Second matrix.

    Returns:
        list of list: Resulting matrix after multiplication.

    Example:
        >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns of A must match number of rows of B.")
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


def conditional_probability(events):
    """
    Calculate conditional probability: P(A | B) = P(A and B) / P(B)

    Args:
        events (dict): Dictionary with keys:
            - 'P(A and B)' (float)
            - 'P(B)' (float)

    Returns:
        float: The conditional probability P(A | B)

    Example:
        >>> conditional_probability({'P(A and B)': 0.12, 'P(B)': 0.3})
        0.4
    """
    p_a_and_b = events.get('P(A and B)')
    p_b = events.get('P(B)')

    if p_b == 0:
        raise ValueError("P(B) cannot be zero.")
    
    return p_a_and_b / p_b
