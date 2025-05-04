from contraction import contract
from expansion   import expand, formula_eq
from resolution  import entails
from copy import deepcopy


def bases_equivalent(kb1: list[str], kb2: list[str]) -> bool:
    """True iff every sentence of one base is entailed by the other."""
    return all(entails(kb2, s) for s in kb1) and \
           all(entails(kb1, s) for s in kb2)


def revise(Kb: list[str], p: str, prio = None) -> list[str]:
    """
    AGM revision of belief base `Kb` by sentence `p`, using Levi Identity.

    Parameters
    ----------
    kb : list[str]
        Current belief base (strings).
    p  : str
        New information to revise with.

    Returns
    -------
    list[str]  --  new belief base (fresh list).
    """
    not_p = f"!({p})"             # syntactically safe negation
    contracted = contract(Kb, not_p, prio)      # gives a *new* list
    revised    = expand(contracted, p)    # add p unless already equivalent
    return revised

def is_consistent(Kb: list[str]) -> bool:
    """
    Returns True iff `kb` is logically consistent,
    implemented only with the higher‑level `entails`.
    """
    # Pick an atom that definitely does *not* occur in the KB
    atom = "__fresh__"
    while any(atom in f for f in Kb):
        atom = "_" + atom            # extend until it is fresh

    # Inconsistency ⇒ KB ⊨ φ  and  KB ⊨ ¬φ   for *every* φ.
    return not (entails(Kb, atom) and entails(Kb, f"!{atom}"))

def test_agm_postulates():
    passed, failed = [], []

    # Base KB and sentence to revise with
    kb      = ["p", "p -> q"]           #   { p , p → q }
    p       = "q"                       # will be added by revision
    p_equiv = "!!q"                     # logically equivalent to q (double neg)

    # ---------- Perform revision once so we can reuse the result ----------
    revised     = revise(deepcopy(kb), p)
    expanded_kb = expand(deepcopy(kb), p)

    # ------------------------------------------------------------------ 1. Success
    if entails(revised, p):
        passed.append("Success")
    else:
        failed.append("Success")

    # --------------------------------------------------------------- 2. Inclusion
    if set(revised).issubset(set(expanded_kb)):
        passed.append("Inclusion")
    else:
        failed.append("Inclusion")

    # ----------------------------------------------------------------- 3. Vacuity
    if not entails(kb, f"!({p})"):                  # ¬p is *not* already entailed
        rev_vac = revise(deepcopy(kb), p)
        exp_vac = expand(deepcopy(kb), p)
        if set(rev_vac) == set(exp_vac):
            passed.append("Vacuity")
        else:
            failed.append("Vacuity")
    else:                                           # Vacuity not applicable
        passed.append("Vacuity (N/A)")

    # -------------------------------------------------------------- 4. Consistency
    if is_consistent(revised):
        passed.append("Consistency")
    else:
        failed.append("Consistency")

    # ------------------------------ 5. Extensionality
    assert formula_eq(p, p_equiv)
    rev1 = revise(deepcopy(kb), p)
    rev2 = revise(deepcopy(kb), p_equiv)

    if bases_equivalent(rev1, rev2):
        passed.append("Extensionality")
    else:
        failed.append("Extensionality")

    return passed, failed


# --------------------------------------------------------------------------- #
# Small CLI hook
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    ok, bad = test_agm_postulates()
    print("Passed:", ok)
    print("Failed:", bad)