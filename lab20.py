# ECB and CBC Error Propagation

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def encrypt(block, key):
    return xor(block, key)


key = b"12345678"
iv = b"ABCDEFGH"

P1 = b"BLOCK001"
P2 = b"BLOCK002"
P3 = b"BLOCK003"

# CBC Encryption
C1 = encrypt(xor(P1, iv), key)
C2 = encrypt(xor(P2, C1), key)
C3 = encrypt(xor(P3, C2), key)

print("Original CBC:")
print(C1.hex(), C2.hex(), C3.hex())

# Introduce an error in C1
C1_error = bytearray(C1)
C1_error[0] ^= 1
C1_error = bytes(C1_error)

# Receiver
D1 = xor(encrypt(C1_error, key), iv)
D2 = xor(encrypt(C2, key), C1_error)
D3 = xor(encrypt(C3, key), C2)

print("\nAfter error in C1:")
print("P1 =", D1)
print("P2 =", D2)
print("P3 =", D3)
