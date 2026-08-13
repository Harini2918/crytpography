# DES Subkey Generation

key = "133457799BBCDFF1"

# PC-1: 64-bit key -> 56-bit key
PC1 = [
57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,
59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,
31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,
29,21,13,5,28,20,12,4
]

# PC-2: 56-bit -> 48-bit subkey
PC2 = [
14,17,11,24,1,5,3,28,15,6,21,10,
23,19,12,4,26,8,16,7,27,20,13,2,
41,52,31,37,47,55,30,40,51,45,33,48,
44,49,39,56,34,53,46,42,50,36,29,32
]

shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

bits = bin(int(key,16))[2:].zfill(64)

key56 = ''.join(bits[i-1] for i in PC1)

C = key56[:28]
D = key56[28:]

for round_no, shift in enumerate(shifts, 1):

    C = C[shift:] + C[:shift]
    D = D[shift:] + D[:shift]

    combined = C + D
    subkey = ''.join(combined[i-1] for i in PC2)

    print("K" + str(round_no) + " =", subkey)
