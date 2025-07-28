from ml_math import dot_product, matrix_multiply, conditional_probability

# Example usage
print(dot_product([1, 2, 3], [4, 5, 6]))                 # 32
print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])) # [[19, 22], [43, 50]]
print(conditional_probability({'P(A and B)': 0.12, 'P(B)': 0.3})) # 0.4
