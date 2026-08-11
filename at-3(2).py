# ============================================================
# 2. BLOCK CIPHER MODES
# ECB / CBC / CFB / OFB
# Standard Python only
# ============================================================

BLOCK_SIZE = 16


def pad(data):
    padding = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([padding]) * padding


def unpad(data):
    padding = data[-1]

    if padding < 1 or padding > BLOCK_SIZE:
        raise ValueError("Invalid padding")

    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding")

    return data[:-padding]


def encrypt_block(block, key):
    return bytes(
        block[i] ^ key[i % len(key)]
        for i in range(BLOCK_SIZE)
    )


def decrypt_block(block, key):
    return encrypt_block(block, key)


# ---------------- ECB ----------------

def ecb_encrypt(data, key):

    data = pad(data)

    result = bytearray()

    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i+BLOCK_SIZE]

        result.extend(
            encrypt_block(block, key)
        )

    return bytes(result)


def ecb_decrypt(data, key):

    result = bytearray()

    for i in range(0, len(data), BLOCK_SIZE):

        block = data[i:i+BLOCK_SIZE]

        result.extend(
            decrypt_block(block, key)
        )

    return unpad(bytes(result))


# ---------------- CBC ----------------

def cbc_encrypt(data, key, iv):

    if len(iv) != BLOCK_SIZE:
        raise ValueError("IV must be 16 bytes")

    data = pad(data)

    result = bytearray()

    previous = iv

    for i in range(0, len(data), BLOCK_SIZE):

        block = data[i:i+BLOCK_SIZE]

        xored = bytes(
            block[j] ^ previous[j]
            for j in range(BLOCK_SIZE)
        )

        encrypted = encrypt_block(xored, key)

        result.extend(encrypted)

        previous = encrypted

    return bytes(result)


def cbc_decrypt(data, key, iv):

    if len(iv) != BLOCK_SIZE:
        raise ValueError("IV must be 16 bytes")

    result = bytearray()

    previous = iv

    for i in range(0, len(data), BLOCK_SIZE):

        block = data[i:i+BLOCK_SIZE]

        decrypted = decrypt_block(block, key)

        plain = bytes(
            decrypted[j] ^ previous[j]
            for j in range(BLOCK_SIZE)
        )

        result.extend(plain)

        previous = block

    return unpad(bytes(result))


# ---------------- CFB ----------------

def cfb_encrypt(data, key, iv):

    result = bytearray()

    previous = iv

    for i in range(0, len(data), BLOCK_SIZE):

        block = data[i:i+BLOCK_SIZE]

        stream = encrypt_block(previous, key)

        cipher = bytes(
            block[j] ^ stream[j]
            for j in range(len(block))
        )

        result.extend(cipher)

        if len(cipher) == BLOCK_SIZE:
            previous = cipher

    return bytes(result)


def cfb_decrypt(data, key, iv):

    result = bytearray()

    previous = iv

    for i in range(0, len(data), BLOCK_SIZE):

        block = data[i:i+BLOCK_SIZE]

        stream = encrypt_block(previous, key)

        plain = bytes(
            block[j] ^ stream[j]
            for j in range(len(block))
        )

        result.extend(plain)

        if len(block) == BLOCK_SIZE:
            previous = block

    return bytes(result)


# ---------------- OFB ----------------

def ofb_crypt(data, key, iv):

    result = bytearray()

    previous = iv

    for i in range(0, len(data), BLOCK_SIZE):

        previous = encrypt_block(previous, key)

        block = data[i:i+BLOCK_SIZE]

        output = bytes(
            block[j] ^ previous[j]
            for j in range(len(block))
        )

        result.extend(output)

    return bytes(result)


# ---------------- TEST ----------------

key = b"1234567890ABCDEF"
iv = b"FEDCBA0987654321"

message = b"This is a secret message."

print("Original:", message)

# ECB
cipher = ecb_encrypt(message, key)
plain = ecb_decrypt(cipher, key)

print("\nECB")
print("Cipher:", cipher.hex())
print("Plain :", plain)

# CBC
cipher = cbc_encrypt(message, key, iv)
plain = cbc_decrypt(cipher, key, iv)

print("\nCBC")
print("Cipher:", cipher.hex())
print("Plain :", plain)

# CFB
cipher = cfb_encrypt(message, key, iv)
plain = cfb_decrypt(cipher, key, iv)

print("\nCFB")
print("Cipher:", cipher.hex())
print("Plain :", plain)

# OFB
cipher = ofb_crypt(message, key, iv)
plain = ofb_crypt(cipher, key, iv)

print("\nOFB")
print("Cipher:", cipher.hex())
print("Plain :", plain)
