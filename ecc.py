# Ultra-minimal ECC implementation - for educational purposes only

# Input elliptic curve parameters and base point
p, a, b = map(int, input("Enter curve parameters (p a b): ").split())
Gx, Gy = map(int, input("Enter base point (Gx Gy): ").split())
private_key = int(input("Enter your private key (d): "))

# Function to add two points on the elliptic curve
def add(P1, P2):
    if P1 is None: return P2
    if P2 is None: return P1
    if P1[0] == P2[0] and (P1[1] != P2[1] or P1[1] == 0): return None
    if P1 == P2:
        lam = (3 * P1[0]**2 + a) * pow(2 * P1[1], p - 2, p) % p
    else:
        lam = (P2[1] - P1[1]) * pow(P2[0] - P1[0], p - 2, p) % p
    x3 = (lam**2 - P1[0] - P2[0]) % p
    y3 = (lam * (P1[0] - x3) - P1[1]) % p
    return (x3, y3)

# Scalar multiplication: d * G
def multiply(k, point):
    result = None
    while k:
        if k & 1:
            result = add(result, point)
        point = add(point, point)
        k >>= 1
    return result

# Compute and display public key
G = (Gx, Gy)
public_key = multiply(private_key, G)
print(f"Public key: {public_key}")
