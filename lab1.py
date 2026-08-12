def caesar_cipher(text, k):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + k) % 26 + base)
        else:
            result += ch

    return result


text = input("Enter the text: ")
k = int(input("Enter key (1-25): "))

if 1 <= k <= 25:
    encrypted = caesar_cipher(text, k)
    print("Encrypted text:", encrypted)
else:
    print("Key must be between 1 and 25")
