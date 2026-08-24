# One-Time Pad Vigenere Cipher

plaintext = input("Enter plaintext: ").upper()
key = list(map(int, input("Enter key numbers: ").split()))

ciphertext = ""

for i in range(len(plaintext)):
    if plaintext[i].isalpha():
        p = ord(plaintext[i]) - ord('A')
        c = (p + key[i]) % 26
        ciphertext += chr(c + ord('A'))

print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)
