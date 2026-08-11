# Simple RSA
p = 11
q = 13

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = pow(e, -1, phi)

m = 9

c = pow(m, e, n)
plain = pow(c, d, n)

print("Public key :", (e, n))
print("Private key:", (d, n))
print("Encrypted  :", c)
print("Decrypted  :", plain)
