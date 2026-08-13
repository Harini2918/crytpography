# CBC Mode Encryption
# Security: 3DES is stronger than DES
# Performance: DES is faster, but 3DES is safer

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def simple_encrypt(block, key):
    return bytes((block[i] ^ key[i % len(key)]) for i in range(len(block)))


def cbc_encrypt(text, key, iv):
    data = text.encode()

    # Padding
    while len(data) % 8 != 0:
        data += b' '

    previous = iv
    result = b''

    for i in range(0, len(data), 8):
        block = data[i:i+8]

        # CBC: Plaintext XOR previous ciphertext
        x = xor(block, previous)

        # Encryption
        encrypted = simple_encrypt(x, key)

        result += encrypted
        previous = encrypted

    return result


text = input("Enter plaintext: ")
key = b"12345678"
iv = b"ABCDEFGH"

cipher = cbc_encrypt(text, key, iv)

print("Ciphertext:", cipher.hex())

print("\n(a) Security: Choose 3DES")
print("(b) Performance: Choose DES")
