from math import gcd

n = 3599

m = int(input("Enter the plaintext block: "))

p = gcd(m, n)

if p > 1:
    q = n // p
    print("Factor p =", p)
    print("Factor q =", q)
    print("RSA can be broken")
else:
    print("No common factor found")
