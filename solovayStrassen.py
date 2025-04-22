def jacobi(a, n):
    r = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]: r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def solovayStrassen(a, N):
    if N < 2 or N % 2 == 0: print("Composite"); return
    j = jacobi(a, N) % N
    p = pow(a, (N-1)//2, N)
    print("Probably Prime" if p == j else "Composite")

N = int(input("Enter the value of N: "))
a = 2
solovayStrassen(a, N)
