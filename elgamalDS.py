import random
import hashlib

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def elgamal_signature():
    print("\n--- ElGamal Digital Signature ---")

    p = int(input("Enter prime p: "))
    g = int(input("Enter generator g: "))
    x = int(input("Enter private key x: "))     # Private key
    y = pow(g, x, p)                             # Public key

    M = input("Enter message: ")
    h = int(hashlib.sha1(M.encode()).hexdigest(), 16)

    while True:
        k = random.randint(2, p - 2)
        if modinv(k, p - 1): break

    r = pow(g, k, p)
    k_inv = modinv(k, p - 1)
    s = (k_inv * (h - x * r)) % (p - 1)

    print(f"Signature: (r, s) = ({r}, {s})")

    # Verification
    v1 = (pow(y, r, p) * pow(r, s, p)) % p
    v2 = pow(g, h, p)
    print("Signature valid!" if v1 == v2 else "Signature invalid!")

elgamal_signature()
