from resolution import entails 

def formula_eq(f1: str, f2: str) -> bool:
    """
    Logical equivalence based on resolution.
    Returns True iff f1 ⟺ f2 is a tautology, i.e.
      • f1 ⊨ f2  and
      • f2 ⊨ f1
    """
    return entails([f1], f2) and entails([f2], f1)

def expand(Kb, f) -> list:
    """
    Parameters
    ----------
    kb       list[str]   belief set (strings)
    f         str        formula to be added

    Returns
    -------
    list      new belief base (shallow copy)
    """
    for belief in Kb:
        if formula_eq(belief, f):
            return Kb               # nothing to add
    Kb.append(f)
    return Kb