from math import sqrt

type_de_polyedre = str(input())
a = float(input())

T = (sqrt(2) / 12) * (a ** 3)
C = a ** 3
O = (sqrt(2) / 3) * (a ** 3)
D = ((15 + (7 * sqrt(5))) / 4) * (a ** 3)
I = ((5 * (3 + sqrt(5))) / 12) * (a ** 3)

if type_de_polyedre == "T":
    print(T)
elif type_de_polyedre == "C":
    print(C)
elif type_de_polyedre == "O":
    print(O)
elif type_de_polyedre == "D":
    print(D)
elif type_de_polyedre == "I":
    print(I)
else:
    print("Polyèdre non connu")
