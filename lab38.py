# Hill Cipher

import numpy as np

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    result = ""

    for i in range(0, len(text), 2):
        p1 = ord(text[i]) - 65
        p2 = ord(text[i + 1]) - 65

        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

        result += chr(c1 + 65) + chr(c2 + 65)

    return result


key = [[3, 3],
       [2, 5]]

plaintext = input("Enter plaintext (even length): ")

ciphertext = hill_encrypt(plaintext, key)

print("Plaintext :", plaintext.upper())
print("Ciphertext:", ciphertext)
