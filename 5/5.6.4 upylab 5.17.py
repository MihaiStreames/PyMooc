def decompresse(l):
    return [c for (n, v) in l for c in [v] * n]
