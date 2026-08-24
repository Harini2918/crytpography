# Frequency Attack on Additive Cipher

freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

cipher = input("Enter ciphertext: ").upper()
n = int(input("Enter number of possible plaintexts: "))

# Try all 26 possible shifts
results = []

for key in range(26):
    plaintext = ""

    for ch in cipher:
        if ch.isalpha():
            p = (ord(ch) - 65 - key) % 26
            plaintext += chr(p + 65)
        else:
            plaintext += ch

    # Simple score based on common English letters
    score = 0
    for ch in plaintext:
        if ch in freq[:10]:
            score += 1

    results.append((score, key, plaintext))

# Sort by likelihood
results.sort(reverse=True)

print("\nPossible plaintexts:")

for i in range(min(n, 26)):
    score, key, plaintext = results[i]
    print(i + 1, ".", plaintext, "(Key =", key, ")")
