import itertools
from resolution import entails


def contract(kb, p):
    if not entails(kb, p):
        return kb
    
    remainders =[]

    for k in range(1, len(kb) + 1):
        for indices in itertools.combinations(range(len(kb)), k):
            subset = [kb[i] for i in range(len(kb)) if i not in indices]
            if not entails(subset, p):

                is_maxi = True
                for other_indices in itertools.combinations(range(len(kb)), k-1):
                    superset = [kb[i] for i in range(len(kb)) if i not in other_indices]
                    if subset < superset and not entails(superset, p):
                        is_maxi = False
                        break
                    if is_maxi:
                        remainders.append(set(subset))


    # No way to contract
    if not remainders:
        return set()
    
    contracted = set.intersection(*remainders)
    return contracted
