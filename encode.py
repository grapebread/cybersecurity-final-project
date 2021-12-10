import numpy as np

def matrixInv(matrix, modulus):

    det = int(np.round(np.linalg.det(matrix)))  
    determinantInverse = egcd(det, modulus)[1] % modulus  
    matrix_modulus_inv = determinantInverse * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus  
    return matrix_modulus_inv