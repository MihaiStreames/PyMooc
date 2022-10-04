n = int(input())
liste = []

for i in range(1, n + 1):
    l = [str(i * m) for m in range(1, n + 1)]
    liste.append(l)

for n in liste:
    print(" ".join(n))