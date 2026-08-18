X = int(input("Enter message block (0-255): "))
K = int(input("Enter key (0-255): "))

T = X ^ K

second_block = X ^ T

mac = second_block ^ T ^ K

print("CBC-MAC for one-block message (T):", T)
print("Second block (X XOR T):", second_block)
print("CBC-MAC for two-block message:", mac)
