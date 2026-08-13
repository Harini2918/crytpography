import numpy as np

# Known plaintext-ciphertext pairs
# Plaintext:  HELP
# Ciphertext: HIAT
P = np.array([[7, 4],
              [4, 15]])

C = np.array([[7, 0],
              [8, 19]])

# Find inverse of P modulo 26
det = int(round(np.linalg.det(P))) % 26
inv_det = pow(det, -1, 26)

P_inv = np.array([[15, -4],
                  [-4, 7]]) * inv_det % 26

# Recover key: K = C * P^-1 mod 26
K = np.dot(C, P_inv) % 26

print("Recovered Hill Cipher Key:")
print(K.astype(int))
