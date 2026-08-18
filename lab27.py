message = input("Enter the message: ").upper()

encrypted = []

for ch in message:
    if ch.isalpha():
        encrypted.append(ord(ch) - ord('A'))

print("Plaintext values:", encrypted)

if len(set(encrypted)) < len(encrypted):
    print("Repeated patterns found")
    print("The encryption method is not secure")
else:
    print("No repeated patterns found")
