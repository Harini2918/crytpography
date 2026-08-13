# DES Decryption Key Schedule

key = "133457799BBCDFF1"

# DES left-shift schedule
shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# Convert hexadecimal key to binary
bits = bin(int(key, 16))[2:].zfill(64)

# Remove parity bits (PC-1)
pc1 = [
57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,
59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,
31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,
29,21,13,5,28,20,12,4
]

key56 = ''.join(bits[i-1] for i in pc1)

C = key56[:28]
D = key56[28:]

keys = []

for s in shifts:
    C = C[s:] + C[:s]
    D = D[s:] + D[:s]
    keys.append(C + D)

print("DES Decryption Keys:")

for i in range(15, -1, -1):
    print("K" + str(i+1), "=", keys[i])
