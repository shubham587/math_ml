def add_vectors(a, b):
    return [x + y for x, y in zip(a, b)]

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def are_orthogonal(a, b):
    return dot_product(a, b) == 0

def multiply_matrices(A, B):
    rows = len(A)
    cols = len(B[0])
    dim = len(B)

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(dim):
                result[i][j] += A[i][k] * B[k][j]

    return result
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]


print("Matrix Multiplication Result:")
product = multiply_matrices(A, B)
for row in product:
    print(row)


a = [1, 2, 3]
b = [4, 5, 6]

print("Sum:", add_vectors(a, b))
print("Dot Product:", dot_product(a, b))
print("Orthogonal:", are_orthogonal(a, b))
