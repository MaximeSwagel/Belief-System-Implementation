from cnf_conversion import string_to_clauses

def entails(kb, query):
    negated = f"!({query})"
    all_clauses = []
    for formula in kb + [negated]:
        all_clauses.extend(string_to_clauses(formula))

    clause_sets = [set(clause) for clause in all_clauses]

    return resolution(clause_sets)

def resolve(ci, cj):
    for literal in ci:
        complement = literal[1:] if literal.startswith("!") else f"!{literal}"
        if complement in cj:
            new_clause = (ci - {literal}) | (cj - {complement})
            return new_clause
    return None

def resolution(clauses):
    new = set()
    while True:
        pairs = [(clauses[i], clauses[j])
                 for i in range(len(clauses)) for j in range(i + 1, len(clauses))]
        for (ci, cj) in pairs:
            resolvent = resolve(ci, cj)
            if resolvent is not None:
                if not resolvent:
                    return True
                new.add(frozenset(resolvent))
        new_clauses = [set(c) for c in new if set(c) not in clauses]
        if not new_clauses:
            return False
        clauses.extend(new_clauses)

def revise(kb, p):
    if entails(kb, p):
        return kb

    neg_p = f"!({p})"

    if not entails(kb, neg_p):
        return kb + [p]

    contracted_kbs = []
    for i in range(len(kb)):
        subset = kb[:i] + kb[i+1:]
        if not entails(subset, neg_p):
            contracted_kbs.append(subset)

    if not contracted_kbs:
        raise ValueError("No consistent contraction possible.")

    contracted = contracted_kbs[0]

    revised = contracted + [p]
    return revised