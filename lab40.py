# Frequency Attack on Monoalphabetic Substitution Cipher

freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

cipher = input("Enter ciphertext: ").upper()
n = int(input("Enter number of possible plaintexts: "))

# Count letter frequency
count = {}
for ch in cipher:
    if ch.isalpha():
        count[ch] = count.get(ch, 0) + 1

# Arrange letters by frequency
sorted_letters = sorted(count, key=count.get, reverse=True)

print("\nPossible Plaintexts:")

for attempt in range(min(n, 10)):
    plain = ""

    for ch in cipher:
        if ch.isalpha():
            pos = sorted_letters.index(ch)
            plain += freq[(pos + attempt) % 26]
        else:
            plain += ch

    print(attempt + 1, ".", plain)
