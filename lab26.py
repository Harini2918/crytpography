p = 59
q = 61

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

print("Old public key (e, n):", (e, n))
print("Old private key (d, n):", (d, n))

new_e = 31
new_d = pow(new_e, -1, phi)

print("New public key (e, n):", (new_e, n))
print("New private key (d, n):", (new_d, n))

print("Not safe to reuse the same modulus.")
