# ============================================================
# 5. ECC IMPLEMENTATION
# Point Addition
# Point Doubling
# Double-and-Add Scalar Multiplication
# ECC Key Exchange
# Standard Python only
# ============================================================


# Curve:
#
# y^2 = x^3 + ax + b (mod p)

p = 17
a = 2
b = 2

# Point at infinity
O = None


# ---------------- POINT ADDITION ----------------

def point_add(P, Q):

    if P is O:
        return Q

    if Q is O:
        return P

    x1, y1 = P
    x2, y2 = Q

    # P + (-P) = O
    if x1 == x2 and (y1 + y2) % p == 0:
        return O

    # Point doubling
    if P == Q:

        numerator = (3 * x1 * x1 + a) % p
        denominator = (2 * y1) % p

        if denominator == 0:
            return O

        slope = (
            numerator *
            pow(denominator, -1, p)
        ) % p

    else:

        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p

        slope = (
            numerator *
            pow(denominator, -1, p)
        ) % p

    x3 = (
        slope * slope -
        x1 -
        x2
    ) % p

    y3 = (
        slope * (x1 - x3) -
        y1
    ) % p

    return (x3, y3)


# ---------------- DOUBLE AND ADD ----------------

def scalar_multiply(k, point):

    result = O
    current = point

    while k > 0:

        if k & 1:
            result = point_add(
                result,
                current
            )

        current = point_add(
            current,
            current
        )

        k >>= 1

    return result


# ---------------- TEST CURVE ----------------

G = (5, 1)

print("ECC CURVE")
print("----------------")

print("Curve:")
print(
    f"y² = x³ + {a}x + {b} (mod {p})"
)

print("Base point:", G)


# ---------------- KEY GENERATION ----------------

alice_private = 5
bob_private = 7

alice_public = scalar_multiply(
    alice_private,
    G
)

bob_public = scalar_multiply(
    bob_private,
    G
)


print("\nAlice Private:", alice_private)
print("Alice Public :", alice_public)

print("\nBob Private:", bob_private)
print("Bob Public :", bob_public)


# ---------------- SHARED SECRET ----------------

alice_shared = scalar_multiply(
    alice_private,
    bob_public
)

bob_shared = scalar_multiply(
    bob_private,
    alice_public
)


print("\nAlice Shared:", alice_shared)
print("Bob Shared  :", bob_shared)

print(
    "\nShared keys match:",
    alice_shared == bob_shared
)
