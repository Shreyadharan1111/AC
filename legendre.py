def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

a = int(input("Enter a: "))
p = int(input("Enter an odd prime p: "))

symbol = legendre(a, p)
if symbol == p - 1:
    symbol = -1

print(f"Legendre symbol ({a}/{p}) = {symbol}")
