n = int(input("Nombre de termes a calculer? "))

x = 0
y = 1

termes = [x, y]

for i in range(n-2):
    x, y = y, x + y
    termes.append(y)
print(termes)