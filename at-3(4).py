# Diffie-Hellman Key Exchange
p = 23
g = 5

alice_private = 6
bob_private = 15

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

alice_key = pow(bob_public, alice_private, p)
bob_key = pow(alice_public, bob_private, p)

print("Alice public:", alice_public)
print("Bob public  :", bob_public)

print("Alice key:", alice_key)
print("Bob key  :", bob_key)

print("Keys match:", alice_key == bob_key)
