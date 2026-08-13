def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    text = ""

    for ch in key + alphabet:
        if ch in alphabet and ch not in text:
            text += ch

    return [text[i:i+5] for i in range(0, 25, 5)]


def decrypt_playfair(ciphertext, key):
    matrix = create_matrix(key)

    # Remove spaces and new lines
    ciphertext = "".join(ciphertext.split()).upper()

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        a = ciphertext[i]
        b = ciphertext[i + 1]

        r1 = c1 = r2 = c2 = 0

        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    r1, c1 = r, c
                if matrix[r][c] == b:
                    r2, c2 = r, c

        # Same row
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]

        # Same column
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]

        # Rectangle
        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ"""

key = input("Enter Playfair key: ")

print("\nDecrypted message:")
print(decrypt_playfair(ciphertext, key))
