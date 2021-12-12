import sys
import numpy as np

"""
returns the inverse of the matrix parameter in mod 26
matrix represents some invertible matrix (square numpy array with a non-zero determinant)
"""
def inv(matrix):
    det = int(np.linalg.det(matrix))
    print(det)
    x = 0
    while ((det * x) % 26 != 1): x += 1

    adj = [[matrix[1][1], -1 * matrix[0][1]], [-1 * matrix[1][0], matrix[0][0]]]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            adj[i][j] *= x
            adj[i][j] %= 26

    return adj


"""
cipher_matrix is a n-component vector (i.e [1, 2, 3, 4, 5])
key is a square matrix (i.e [[1, 2], [3, 4]] where the number of elements
must be a perfect square)
key must also be an invertible matrix (hence have a zero determinant)
"""
def decode(cipher_matrix, key):
    plain_matrix = np.array()

    return plain_matrix