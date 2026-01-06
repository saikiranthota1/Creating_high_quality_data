import random

def weighted_choice(items):
    total = sum(w for _, w in items)
    r = random.uniform(0, total)
    upto = 0
    for val, w in items:
        if upto + w >= r:
            return val
        upto += w
