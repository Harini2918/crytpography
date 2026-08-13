import numpy as np

key = np.array([[9, 4], [5, 7]])

text = "meet me at the usual place at ten rather than eight oclock"
text = ''.join(c for c in text.lower() if c.isalpha())

# Add X if length is odd
if len(text) % 2:
    text += 'x'

# Encryption
cipher = ""

for i in range(0, len(text), 2):
    x = np.array([[ord(text[i])-97],
                  [ord(text[i+1])-97]])

    y = np.dot(key, x) % 26

    cipher += chr(y[0][0]+97)
    cipher += chr(y[1][0]+97)

print("Ciphertext:", cipher)

# Decryption
det = int(np.linalg.det(key)) % 26
inv_det = pow(det, -1, 26)

inverse = np.array([[7, -4],
                    [-5, 9]]) * inv_det % 26

plain = ""

for i in range(0, len(cipher), 2):
    x = np.array([[ord(cipher[i])-97],
                  [ord(cipher[i+1])-97]])

    y = np.dot(inverse, x) % 26

    plain += chr(y[0][0]+97)
    plain += chr(y[1][0]+97)

print("Decrypted:", plain)
