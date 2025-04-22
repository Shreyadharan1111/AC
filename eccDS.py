import random
import hashlib

# Curve parameters for y^2 = x^3 + ax + b mod p
a, b, p = 2, 3, 97
G = (3, 6)  # Base point

def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def point_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    if P[0] == Q[0] and (P[1] != Q[1] or P[1] == 0): return None

    if P == Q:
        l = (3 * P[0]**2 + a) * modinv(2 * P[1], p)
    else:
        l = (Q[1] - P[1]) * modinv(Q[0] - P[0], p)
    l = l % p
    x = (l**2 - P[0] - Q[0]) % p
    y = (l * (P[0] - x) - P[1]) % p
    return (x, y)

def scalar_mult(k, P):
    R = None
    while k > 0:
        if k & 1:
            R = point_add(R, P)
        P = point_add(P, P)
        k >>= 1
    return R

def ecc_signature():
    print("\n--- ECC Digital Signature ---")
    d = random.randint(1, 20)         # Private key
    Q = scalar_mult(d, G)             # Public key

    M = input("Enter message: ")
    h = int(hashlib.sha1(M.encode()).hexdigest(), 16)

    while True:
        k = random.randint(1, p - 2)
        R = scalar_mult(k, G)
        if R is None: continue
        r = R[0] % p
        if r == 0: continue
        k_inv = modinv(k, p)
        if not k_inv: continue
        s = (k_inv * (h + r * d)) % p
        if s != 0: break

    print(f"Private Key d = {d}")
    print(f"Public Key Q = {Q}")
    print(f"Signature: (r, s) = ({r}, {s})")

    # Verification
    w = modinv(s, p)
    u1 = (h * w) % p
    u2 = (r * w) % p
    P1 = scalar_mult(u1, G)
    P2 = scalar_mult(u2, Q)
    V = point_add(P1, P2)
    if V and V[0] % p == r:
        print("✅ Signature valid!")
    else:
        print("❌ Signature invalid!")

ecc_signature()
