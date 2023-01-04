n = int(input("Valeur du nombre n dont on veut tester la conjecture: "))
n_initial = n

etapes = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
        etapes = etapes + 1
    else:
        n = 3 * n + 1
        etapes = etapes + 1
print(f"Etapes pour la conjecture de {n_initial}: {etapes}")
