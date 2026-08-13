def keyword_cipher(text, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Create cipher alphabet using keyword
    cipher = ""
    for ch in keyword.lower() + alphabet:
        if ch in alphabet and ch not in cipher:
            cipher += ch

    result = ""

    for ch in text.lower():
        if ch in alphabet:
            result += cipher[alphabet.index(ch)]
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
keyword = input("Enter keyword: ")

print("Ciphertext:", keyword_cipher(text, keyword))
