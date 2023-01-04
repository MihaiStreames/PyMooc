from math import sqrt

a = float(input())
b = float(input())

if a < 0 or b < 0:
    print("Erreur")
    exit()

moyenne_geo = sqrt(a * b)
print(moyenne_geo)
