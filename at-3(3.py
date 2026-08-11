# ============================================================
# 3. RSA IMPLEMENTATION
# Prime generation
# Fast modular exponentiation
# CRT optimization
# ============================================================

import random
import math


# ---------------- PRIME TEST ----------------

def is_prime(n):

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    i = 3

    while i * i <= n:

        if n % i == 0:
            return False

        i += 2

    return True


def generate_prime(bits=16):

    while True:

        number = random.getrandbits(bits)

        number |= (1 << bits - 1)
        number |= 1

        if is_prime(number):
            return number


# ---------------- KEY GENERATION ----------------

def generate_keys():

    p = generate_prime(16)
    q = generate_prime(16)

    while q == p:
        q = generate_prime(16)

    n = p * q

    phi = (p - 1) * (q - 1)

    e = 65537

    if math.gcd(e, phi) != 1:

        e = 3

        while math.gcd(e, phi) != 1:
            e += 2

    d = pow(e, -1, phi)

    return p, q, n, e, d


# ---------------- RSA ENCRYPTION ----------------

def rsa_encrypt(message, e, n):

    if message >= n:
        raise ValueError(
            "Message is too large for this RSA key"
        )

    return pow(message, e, n)


# ---------------- NORMAL DECRYPTION ----------------

def rsa_decrypt(cipher, d, n):

    return pow(cipher, d, n)


# ---------------- CRT DECRYPTION ----------------

def rsa_decrypt_crt(cipher, p, q, d):

    dp = d % (p - 1)
    dq = d % (q - 1)

    m1 = pow(cipher, dp, p)
    m2 = pow(cipher, dq, q)

    q_inverse = pow(q, -1, p)

    h = (q_inverse * (m1 - m2)) % p

    message = m2 + h * q

    return message


# ---------------- MAIN ----------------

p, q, n, e, d = generate_keys()

print("RSA PARAMETERS")
print("----------------")
print("p =", p)
print("q =", q)
print("n =", n)
print("e =", e)
print("d =", d)

message = 12345

print("\nOriginal message:", message)

cipher = rsa_encrypt(
    message,
    e,
    n
)

print("Encrypted:", cipher)

plain1 = rsa_decrypt(
    cipher,
    d,
    n
)

print("Decrypted:", plain1)

plain2 = rsa_decrypt_crt(
    cipher,
    p,
    q,
    d
)

print("CRT Decrypted:", plain2)

if message == plain2:
    print("\nRSA TEST PASSED")
else:
    print("\nRSA TEST FAILED")
