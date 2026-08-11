p = 17
a = 2
G = (5, 1)

def add(P, Q):
    x1,y1 = P
    x2,y2 = Q
    m = ((y2-y1) * pow(x2-x1, -1, p)) % p
    return ((m*m-x1-x2)%p, (m*(x1-(m*m-x1-x2)%p)-y1)%p)

def multiply(k, P):
    R = P
    for i in range(k-1):
        R = add(R, P)
    return R

private = 3
public = multiply(private, G)

print("Private key:", private)
print("Public key:", public)
