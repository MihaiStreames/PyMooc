def longueur(*p):
    if len(p) < 2: return 0
    origin = p[0]
    acc = 0
    for p in p[1:]:
        acc += distance_points(origin, p)
        origin = p
    return acc


def distance_points(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return (dx * dx + dy * dy) ** .5
