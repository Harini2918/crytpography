# ECB, CBC and CFB Modes
# Simple demonstration without external modules

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def encrypt_block(block, key):
    return xor(block, key)


def decrypt_block(block, key):
    return xor(block, key)


def pad(data, size):
    padding = size - (len(data) % size)
    if padding == 0:
        padding = size
    return data + bytes([0x80]) + bytes(padding - 1)


def ecb_encrypt(data, key):
    result = b""
    for i in range(0, len(data), len(key)):
        result += encrypt_block(data[i:i+len(key)], key)
    return result


def cbc_encrypt(data, key, iv):
    result = b""
    previous = iv

    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]
        block = xor(block, previous)
        encrypted = encrypt_block(block, key)
        result += encrypted
        previous = encrypted

    return result


def cfb_encrypt(data, key, iv):
    result = b""
    previous = iv

    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]
        encrypted = encrypt_block(previous, key)
        cipher = xor(block, encrypted)
        result += cipher
        previous = cipher

    return result


# Input
plaintext = input("Enter plaintext: ").encode()
key = input("Enter key (same length as block): ").encode()
iv = input("Enter IV (same length as key): ").encode()

# Padding
plaintext = pad(plaintext, len(key))

print("\nECB :", ecb_encrypt(plaintext, key).hex())
print("CBC :", cbc_encrypt(plaintext, key, iv).hex())
print("CFB :", cfb_encrypt(plaintext, key, iv).hex())
