import random
import math

# ---------- RSA Section ----------
def rsa_encrypt(M, e, n):
    return pow(M, e, n)

def rsa_decrypt(cipher, d, n):
    return pow(cipher, d, n)

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def rsa_homomorphic():
    print("\n--- RSA Homomorphic Multiplication ---")
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    e = int(input("Enter public key e: "))
    m1 = int(input("Enter message m1: "))
    m2 = int(input("Enter message m2: "))

    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)

    c1 = rsa_encrypt(m1, e, n)
    c2 = rsa_encrypt(m2, e, n)
    c_mult = (c1 * c2) % n
    decrypted = rsa_decrypt(c_mult, d, n)

    print(f"Encrypted m1: {c1}")
    print(f"Encrypted m2: {c2}")
    print(f"Encrypted (m1 * m2): {c_mult}")
    print(f"Decrypted result: {decrypted}")

# ---------- Paillier Section ----------
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

def L(u, n):
    return (u - 1) // n

def paillier_keygen(bit_length=8):
    while True:
        p = random.getrandbits(bit_length)
        q = random.getrandbits(bit_length)
        if math.gcd(p * q, (p - 1) * (q - 1)) == 1 and p != q:
            break
    n = p * q
    nsq = n * n
    g = n + 1
    lam = lcm(p - 1, q - 1)
    u = pow(g, lam, nsq)
    mu = modinv(L(u, n), n)
    return (n, g), (lam, mu)

def paillier_encrypt(m, pubkey):
    n, g = pubkey
    nsq = n * n
    r = random.randint(1, n - 1)
    while math.gcd(r, n) != 1:
        r = random.randint(1, n - 1)
    c = (pow(g, m, nsq) * pow(r, n, nsq)) % nsq
    return c

def paillier_decrypt(c, pubkey, privkey):
    n, g = pubkey
    lam, mu = privkey
    nsq = n * n
    u = pow(c, lam, nsq)
    l_val = L(u, n)
    m = (l_val * mu) % n
    return m

def paillier_homomorphic():
    print("\n--- Paillier Homomorphic Addition ---")
    pub, priv = paillier_keygen()
    n, _ = pub

    m1 = int(input("Enter message m1: "))
    m2 = int(input("Enter message m2: "))

    c1 = paillier_encrypt(m1, pub)
    c2 = paillier_encrypt(m2, pub)

    c_sum = (c1 * c2) % (n * n)
    decrypted = paillier_decrypt(c_sum, pub, priv)

    print(f"Encrypted m1: {c1}")
    print(f"Encrypted m2: {c2}")
    print(f"Encrypted (m1 + m2): {c_sum}")
    print(f"Decrypted result: {decrypted}")

# ---------- Menu ----------
while True:
    print("\n========= Homomorphic Encryption Menu =========")
    print("1. RSA Homomorphic Multiplication")
    print("2. Paillier Homomorphic Addition")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        rsa_homomorphic()
    elif choice == '2':
        paillier_homomorphic()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
