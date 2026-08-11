# ============================================================
# 4. DIFFIE-HELLMAN KEY EXCHANGE
# Standard Python only
# ============================================================

import hashlib
import secrets
import time


# Large demonstration prime
P = 2305843009213693951

# Generator
G = 5


def generate_private_key():
    return secrets.randbelow(P - 2) + 2


def generate_public_key(private_key):

    return pow(
        G,
        private_key,
        P
    )


def generate_shared_key(
        private_key,
        other_public_key):

    return pow(
        other_public_key,
        private_key,
        P
    )


def derive_key(shared_secret):

    return hashlib.sha256(
        str(shared_secret).encode()
    ).hexdigest()


# ---------------- ALICE ----------------

alice_private = generate_private_key()

alice_public = generate_public_key(
    alice_private
)


# ---------------- BOB ----------------

bob_private = generate_private_key()

bob_public = generate_public_key(
    bob_private
)


# ---------------- SHARED SECRET ----------------

start = time.time()

alice_shared = generate_shared_key(
    alice_private,
    bob_public
)

bob_shared = generate_shared_key(
    bob_private,
    alice_public
)

end = time.time()


print("DIFFIE-HELLMAN")
print("--------------------------")

print("Alice Public Key :", alice_public)
print("Bob Public Key   :", bob_public)

print("\nAlice Shared Key :", alice_shared)
print("Bob Shared Key   :", bob_shared)

print("\nKeys match:", alice_shared == bob_shared)

print("Time:",
      end - start,
      "seconds")


# ---------------- KEY DERIVATION ----------------

final_key = derive_key(
    alice_shared
)

print("\nDerived SHA-256 Key:")
print(final_key)
