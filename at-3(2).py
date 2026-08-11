# Simple block cipher mode demonstration
def xor(a, b):
    return ''.join(
        chr(ord(x) ^ ord(y))
        for x, y in zip(a, b)
    )

text = "HELLO123"
key = "12345678"

# ECB
ecb = xor(text, key)
print("ECB:", ecb)

# CBC
iv = "ABCDEFGH"
cbc = xor(xor(text, key), iv)
print("CBC:", cbc)

# CFB
cfb = xor(text, key)
print("CFB:", cfb)

# OFB
ofb = xor(text, key)
print("OFB:", ofb)
