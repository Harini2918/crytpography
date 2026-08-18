counter = 0

plaintext = input("Enter 24-bit plaintext: ")

blocks = [plaintext[i:i + 8] for i in range(0, len(plaintext), 8)]

ciphertext = ""

for block in blocks:
    ctr = format(counter, "08b")
    cipher = format(int(block, 2) ^ int(ctr, 2), "08b")
    ciphertext += cipher
    counter += 1

print("Ciphertext:", ciphertext)

counter = 0
decrypted = ""

for i in range(0, len(ciphertext), 8):
    block = ciphertext[i:i + 8]
    ctr = format(counter, "08b")
    plain = format(int(block, 2) ^ int(ctr, 2), "08b")
    decrypted += plain
    counter += 1

print("Decrypted plaintext:", decrypted)
