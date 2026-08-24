# Simple DES Encryption and Decryption
# No external module required

def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return result


def decrypt(text, key):
    return encrypt(text, key)


plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print("\nPlaintext  :", plaintext)
print("Ciphertext :", ciphertext.encode().hex())
print("Decrypted  :", decrypted)
