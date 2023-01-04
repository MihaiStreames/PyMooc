position_courante = 0
saut = int(input())
position_cible = int(input())

while True:
    position_courante += saut
    if position_courante > 99:
        position_courante -= 100
    if position_courante == position_cible:
        print("Cible atteinte")
        break
    if position_courante == 0:
        print(f"{position_courante}\nPas trouvée")
        break
    print(position_courante)
