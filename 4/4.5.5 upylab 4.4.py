import random


def alea_dice(s):
    random.seed(s)

    dices = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    if sorted(dices) == [1, 2, 4]:
        return True
    else:
        return False
