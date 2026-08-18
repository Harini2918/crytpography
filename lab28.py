q = 23
a = 5

alice_secret = 6
bob_secret = 15

alice_public = (a ** alice_secret) % q
bob_public = (a ** bob_secret) % q

alice_key = (bob_public ** alice_secret) % q
bob_key = (alice_public ** bob_secret) % q

print("Alice's public value:", alice_public)
print("Bob's public value:", bob_public)

print("Alice's shared key:", alice_key)
print("Bob's shared key:", bob_key)
