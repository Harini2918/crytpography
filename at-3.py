# Simple DES-like encryption demonstration

def encrypt(text, key):
    return ''.join(
        chr(ord(c) ^ ord(key[i % len(key)]))
        for i, c in enumerate(text)
    )

text = input("Enter text: ")
key = "1234"

cipher = encrypt(text, key)
plain = encrypt(cipher, key)

print("Encrypted:", cipher)
print("Decrypted:", plain)
