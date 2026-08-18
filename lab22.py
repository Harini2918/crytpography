iv = "10101010"
key = "0111111101"

plaintext = input("Enter 16-bit plaintext: ")

block1 = plaintext[:8]
block2 = plaintext[8:]

cipher1 = format(int(block1, 2) ^ int(iv, 2), "08b")
cipher2 = format(int(block2, 2) ^ int(cipher1, 2), "08b")

ciphertext = cipher1 + cipher2

print("Ciphertext:", ciphertext)

plain1 = format(int(cipher1, 2) ^ int(iv, 2), "08b")
plain2 = format(int(cipher2, 2) ^ int(cipher1, 2), "08b")

decrypted = plain1 + plain2

print("Decrypted plaintext:", decrypted)
