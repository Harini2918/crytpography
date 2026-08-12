def encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for ch in text.upper():
        if ch in alphabet:
            result += key[alphabet.index(ch)]
        else:
            result += ch

    return result


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input("Enter 26-letter key: ").upper()

if len(key) == 26 and len(set(key)) == 26:
    text = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(text, key))
else:
    print("Key must contain 26 unique letters.")
