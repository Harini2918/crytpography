def vigenere(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
key = input("Enter key: ")

print("Ciphertext:", vigenere(text, key))
