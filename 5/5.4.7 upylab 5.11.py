def intersection(v, w):
    ix = ''
    min_ = min(len(v), len(w))
    for s in range(len(v)):
        if len(ix) >= min_ - s:
            break
        for e in range(s + len(ix), min_):
            t = v[s:e + 1]
            if t not in w:
                break
            if len(t) >= len(ix):
                ix = t
    return ix
