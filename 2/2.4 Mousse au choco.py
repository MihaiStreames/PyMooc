""" Auteur: Bors Mihai
    Date : Septembre 2022
    But du programme :
    Calculer le nombre d'ingredients pour faire une mousse au chocolat pour n personnes
    Entrée: Personnes (int)
    Sorties: Nombre d'ingredients par rapport au nombre n de personnes
"""

#Nombre de personnes + verification si c'est un nombre

while True:
    try:
        guests = int(input("Combien de personnes?"))
    except ValueError:
        print("Vous avez mis un nombre invalide de personnes :(")
        continue
    else:
        break

#Valeurs des ingredients

oeufs = int((3 / 4) * guests)
chocolat = int((100 / 4) * guests)
sucre_vanille = int((1 / 4)* guests)

#Au cas ou on met un nombre de personnes inferieur a 3

if oeufs < 1:
    oeufs = oeufs + 1

if sucre_vanille < 1:
    sucre_vanille = sucre_vanille + 1

#Print le resultat

print(f"Pour {guests} personnes il y aurait besoin de {oeufs} oeuf(s),\n{chocolat} grammes de chocolat,\net {sucre_vanille} sachet(s) de vanille!")