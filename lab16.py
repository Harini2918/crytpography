from collections import Counter

freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

cipher = input("Enter ciphertext: ")
n = int(input("Enter number of plaintexts: "))

count = Counter(c for c in cipher.upper() if c.isalpha())
common = [x for x, y in count.most_common()]

results = []

for shift in range(26):
    key = {}

    for i, c in enumerate(common):
        key[c] = freq[(i + shift) % 26]

    text = ""
    for c in cipher.upper():
        text += key.get(c, c)

    score = sum(text.count(x) for x in ["THE", "AND", "ING", "IS", "OF"])
    results.append((score, text))

results.sort(reverse=True)

print("\nTop possible plaintexts:")

for i, (score, text) in enumerate(results[:n], 1):
    print(i, ":", text)
