# Letter Frequency Attack

freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

cipher = input("Enter ciphertext: ").upper()
n = int(input("Enter number of possible plaintexts: "))

letters = []
for ch in cipher:
    if ch.isalpha() and ch not in letters:
        letters.append(ch)

# Sort cipher letters by frequency
count = {}
for ch in cipher:
    if ch.isalpha():
        count[ch] = count.get(ch, 0) + 1

sorted_letters = sorted(count, key=count.get, reverse=True)

# Generate possible plaintexts
for attempt in range(min(n, len(sorted_letters))):
    mapping = {}

    for i, ch in enumerate(sorted_letters):
        mapping[ch] = freq[(i + attempt) % 26]

    plaintext = ""
    for ch in cipher:
        if ch.isalpha():
            plaintext += mapping[ch]
        else:
            plaintext += ch

    print("Possible", attempt + 1, ":", plaintext)
