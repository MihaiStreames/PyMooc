def distance_mots(a, b):
    return abs(len(a) - len(b)) + sum([a[i] != b[i] for i in range(0, min(len(a), len(b)))])
