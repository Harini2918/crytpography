block_size = 8

plaintext = input("Enter the plaintext: ")

padding = block_size - (len(plaintext) % block_size)

if padding == 0:
    padding = block_size

plaintext += "1" + "0" * (padding - 1)

print("Padded plaintext:", plaintext)

print("ECB Mode:", plaintext)
print("CBC Mode:", plaintext)
print("CFB Mode:", plaintext)
