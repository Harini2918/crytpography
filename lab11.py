import math

# Playfair uses 25 letters in a 5 x 5 matrix
keys = math.factorial(25)

print("Total possible keys:", keys)
print("Approximate power of 2:", math.log2(keys))

# Taking equivalent keys into account
unique = keys // (25 * 24)
print("Effectively unique keys:", unique)
print("Approximate power of 2:", math.log2(unique))
