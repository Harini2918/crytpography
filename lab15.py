from collections import Counter

freq = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5,
    'I': 7.0, 'N': 6.7, 'S': 6.3, 'H': 6.1,
    'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8,
    'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2,
    'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}

cipher = input("Enter ciphertext: ").upper()
n = int(input("How many possible plaintexts? "))

results = []

for key in range(26):
    text = ""

    for ch in cipher:
        if ch.isalpha():
            text += chr((ord(ch) - 65 - key) % 26 + 65)
        else:
            text += ch

    score = sum(freq.get(ch, 0) for ch in text)
    results.append((score, key, text))

results.sort(reverse=True)

print("\nPossible plaintexts:")

for score, key, text in results[:n]:
    print("Key:", key, "->", text)
