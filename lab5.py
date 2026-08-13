def affine_cipher(text, a, b):
    result = ""

    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - 65
            c = (a * p + b) % 26
            result += chr(c + 65)
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
    print("Ciphertext:", affine_cipher(text, a, b))
else:
    print("Invalid value of a")
