p = 59
q = 61
e = 31

n = p * q
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
