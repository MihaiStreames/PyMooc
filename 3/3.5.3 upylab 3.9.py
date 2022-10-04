correct = 42

while True:
    rep = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
    if rep == correct:
        print("Bravo !")
        break
    else:
        print("Mauvaise réponse.")