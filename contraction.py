import itertools
from resolution import entails


def contract(kb, p, prio=None):
    if not entails(kb, p):
        return kb
    
    if prio is None:
        prio = list(kb)

    remainders = generate_remainder_sets(kb, p)

    if not remainders:
        return []

    best_score = max(score(r, prio) for r in remainders)
    selected = [r for r in remainders if score(r, prio) == best_score]

    return list(set.intersection(*map(set, selected)))

def score(remainder, prio):
    return sum(len(prio) - prio.index(f) for f in remainder if f in prio) # later beliefs have less priority than earlier beliefs

def generate_remainder_sets(kb, p):
    remainders = []
    n = len(kb)
    for k in range(1, n + 1):
        for indices in itertools.combinations(range(n), k):
            subset = [kb[i] for i in range(n) if i not in indices]
            if not entails(subset, p):
                is_maximal = True
                for j in range(n):
                    if j in indices:
                        new_indices = [i for i in indices if i != j]
                        superset = [kb[i] for i in range(n) if i not in new_indices]
                        if not entails(superset, p):
                            is_maximal = False
                            break
                if is_maximal:
                    remainders.append(subset)
    return remainders