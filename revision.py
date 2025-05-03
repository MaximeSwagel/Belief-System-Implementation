from contraction import contract  
from resolution import entails    
from parser import Parser         
from tokenizer import tokenize
from expansion import expand    
from copy import deepcopy         

# Helper to parse logic strings into AST
def parse(s):
    return Parser(tokenize(s)).parse()

# # Placeholder expansion: simply adds p to the KB if it's not already there
# # Does not check consistency (which would be required in full expansion logic)
# def expand(kb, p_str):
#     p = parse(p_str)
#     if p not in kb:
#         kb.append(p)
#     return kb


# Check if a knowledge base is consistent (does not entail a contradiction)
def is_consistent(kb):
    return not entails([str(f) for f in kb], "a & !a")

# Very simple normalization: eliminate double negation
def normalize_formula_str(s):
    return s.replace("!!", "")

# Normalize full KB to compare logical equivalence (loose string form)
def normalize_kb(kb):
    return set(normalize_formula_str(str(f)).replace("(", "").replace(")", "").strip() for f in kb)

# Revision using Levi Identity: revise(KB, p) = expand(contract(KB, ¬p), p)
def revise(kb, p_str):
    not_p = f"!({p_str})"
    kb_strings = [str(f) for f in kb]      
    contracted = contract(kb_strings, not_p) 
    parsed_kb = [parse(f) for f in contracted]  
    return expand(parsed_kb, p_str)      

# Tests 5 AGM postulates: Success, Inclusion, Vacuity, Consistency, Extensionality
def test_agm_postulates():
    passed, failed = [], []

    kb = [parse("p"), parse("p -> q")]
    p_str = "q"
    revised = revise(deepcopy(kb), p_str)

    # 1. Success
    if any(entails([str(f)], p_str) for f in revised):
        passed.append("Success")
    else:
        failed.append("Success")

    # 2. Inclusion
    expanded = expand(deepcopy(kb), p_str)
    if set(str(f) for f in revised).issubset(set(str(f) for f in expanded)):
        passed.append("Inclusion")
    else:
        failed.append("Inclusion")

    # 3. Vacuity
    if not entails([str(f) for f in kb], f"!({p_str})"):
        revised_vac = revise(deepcopy(kb), p_str)
        expanded_vac = expand(deepcopy(kb), p_str)
        if set(str(f) for f in revised_vac) == set(str(f) for f in expanded_vac):
            passed.append("Vacuity")
        else:
            failed.append("Vacuity")

    # 4. Consistency
    if is_consistent(kb + [parse(p_str)]):
        if is_consistent(revised):
            passed.append("Consistency")
        else:
            failed.append("Consistency")

    # 5. Extensionality
    equivalent_q = f"!!({p_str})"
    revised_eq = revise(deepcopy(kb), equivalent_q)
    normalized_revised = normalize_kb(revised)
    normalized_revised_eq = normalize_kb(revised_eq)

    if normalized_revised == normalized_revised_eq:
        passed.append("Extensionality")
    else:
        failed.append("Extensionality")

    return passed, failed  # ✅ ensure it's outside all if/else

# Run postulate tests when script is executed
if __name__ == "__main__":
    passed, failed = test_agm_postulates()
    print("Passed:", passed)
    print("Failed:", failed)
