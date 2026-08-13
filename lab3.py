def create_matrix(key):
    key = key.upper().replace("J", "I")
    letters = ""

    for ch in key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in letters:
            letters += ch

    return [letters[i:i+5] for i in range(0, 25, 5)]


def encrypt(text, key):
    matrix = create_matrix(key)
    text = text.upper().replace("J", "I").replace(" ", "")

    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"

        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    result = ""

    for a, b in pairs:
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    r1, c1 = r, c
                if matrix[r][c] == b:
                    r2, c2 = r, c

        if r1 == r2:
            result += matrix[r1][(c1+1)%5]
            result += matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1]
            result += matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
text = input("Enter plaintext: ")

print("Ciphertext:", encrypt(text, key))
