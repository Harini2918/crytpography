m = ["MFHIK","UNOPQ","ZVWXY","ELARG","DSTBC"]
p = {m[r][c]:(r,c) for r in range(5) for c in range(5)}
p["J"] = p["I"]

def enc(a,b):
    r1,c1 = p[a]
    r2,c2 = p[b]

    if r1 == r2:
        return m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
    if c1 == c2:
        return m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
    return m[r1][c2] + m[r2][c1]

text = "MUSTSEEYOUOVERCADOGANWESTCOMINGATONCE"
text = text.replace("J","I")

# Make pairs
pairs = []
i = 0
while i < len(text):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else "X"

    if a == b:
        pairs.append(a + "X")
        i += 1
    else:
        pairs.append(a + b)
        i += 2

cipher = ""
for pair in pairs:
    cipher += enc(pair[0], pair[1])

print("Pairs:", " ".join(pairs))
print("Ciphertext:", cipher)
