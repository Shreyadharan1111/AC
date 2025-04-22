def sign(message, d, n):
    return (message ** d) % n

def verify(signature, e, n):
    return (signature ** e) % n

def inverse(a, n):
    b = 2
    while (a * b) % n != 1:
        b += 1
    return b

# Key generation
p = int(input("Enter value of p: "))
q = int(input("Enter value of q: "))
n = p * q
phi = (p - 1) * (q - 1)
e = int(input("Enter public key exponent e: "))
d = inverse(e, phi)

# Signing
message = int(input("Enter message to sign (as number): "))
signature = sign(message, d, n)
print(f"Digital Signature: {signature}")

# Verifying
verified_message = verify(signature, e, n)
print(f"Verified message (after checking signature): {verified_message}")

# Check if signature is valid
if verified_message == message:
    print("Signature is valid.")
else:
    print("Signature is invalid.")
