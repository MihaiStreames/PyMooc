taille = ""
entreprise = []

while taille != -1:
    taille = int(input())
    entreprise.append(taille)
entreprise.remove(-1)

#print(entreprise, len(entreprise))
print(sum(entreprise) / len(entreprise))