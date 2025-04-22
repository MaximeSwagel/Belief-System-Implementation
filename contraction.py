import itertools
from resolution import entails

def contract(kb, p):
    if not entails(kb, p):
        return kb
    
    for k in range(1, len(kb) + 1):
        for indices in itertools.combinations(range(len(kb)), k):
            subset = [kb[i] for i in range(len(kb)) if i not in indices]
            if not entails(subset, p):
                return subset
