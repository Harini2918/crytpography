# One-Time Pad Vigenere Cipher

def encrypt(text, key):
    text = ''.join(c for c in text.lower() if c.isalpha())
    return ''.join(chr((ord(c)-97+k) % 26 + 97)
                   for c, k in zip(text, key))


def find_key(cipher, plaintext):
    return [(ord(c)-ord(p)) % 26
            for c, p in zip(cipher, plaintext)]


# (a)
plaintext = "send more money"
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

cipher = encrypt(plaintext, key)

print("Ciphertext:", cipher)


# (b)
new_plaintext = "cash not needed"

new_key = find_key(cipher, ''.join(c for c in new_plaintext if c.isalpha()))

print("New key:", new_key)

# Verify
print("Decrypted as:", encrypt(new_plaintext, new_key))
