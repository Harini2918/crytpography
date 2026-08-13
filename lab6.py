def affine_encrypt(text, a, b):
    result = ""

    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - 65
            c = (a * p + b) % 26
            result += chr(c + 65)
        else:
            result += ch

    return result


def affine_decrypt(text, a, b):
    result = ""
    inverse = pow(a, -1, 26)

    for ch in text.upper():
        if ch.isalpha():
            c = ord(ch) - 65
            p = (inverse * (c - b)) % 26
            result += chr(p + 65)
        else:
            result += ch

    return result


ciphertext = input("Enter ciphertext: ")

print("Key: a = 3, b = 15")
print("Plaintext:", affine_decrypt(ciphertext, 3, 15))
