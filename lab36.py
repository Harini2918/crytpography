# Affine Caesar Cipher

plaintext = input("Enter plaintext: ").upper()
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

ciphertext = ""

for ch in plaintext:
    if ch.isalpha():
        p = ord(ch) - ord('A')
        c = (a * p + b) % 26
        ciphertext += chr(c + ord('A'))
    else:
        ciphertext += ch

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
