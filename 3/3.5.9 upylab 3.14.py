import random

number = random.randrange(101)
n = 0
guess_limit = 5

while n <= guess_limit:
    guess = int(input())
    n += 1
    if number == guess:
        print("Gagné en", n, "essai(s) !")
        break
    elif number > guess and n <= guess_limit:
        print("Trop petit")
    elif number < guess and n <= guess_limit:
        print("Trop grand")
else:
    print("Perdu ! Le secret était", number)