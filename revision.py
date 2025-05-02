from contraction import contract  
from resolution import entails    
from parser import Parser         
from tokenizer import tokenize
from expansion import expand    
from copy import deepcopy         # For safe testing without modifying original KB

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

# Revision using Levi Identity: revise(KB, p) = expand(contract(KB, ¬p), p)
def revise(kb, p_str):
    not_p = f"!({p_str})"
    kb_strings = [str(f) for f in kb]      
    contracted = contract(kb_strings, not_p) 
    parsed_kb = [parse(f) for f in contracted]  
    return expand(parsed_kb, p_str)         

# Tests 3 AGM postulates: Success, Inclusion, Vacuity
def test_agm_postulates():
    passed, failed = [], []

    # Sample KB: {p, p → q}
    kb = [parse("p"), parse("p -> q")]
    p_str = "q"

    revised = revise(deepcopy(kb), p_str)  # Perform revision

    # AGM Postulate 1: Success — p should be in revised(KB, p)
    if any(entails([str(f)], p_str) for f in revised):
        passed.append("Success")
    else:
        failed.append("Success")

    # AGM Postulate 2: Inclusion — revised KB ⊆ expanded KB
    expanded = expand(deepcopy(kb), p_str)
    if set(str(f) for f in revised).issubset(set(str(f) for f in expanded)):
        passed.append("Inclusion")
    else:
        failed.append("Inclusion")

    # AGM Postulate 3: Vacuity — if ¬p not entailed, revise = expand
    if not entails([str(f) for f in kb], f"!({p_str})"):
        revised_vac = revise(deepcopy(kb), p_str)
        expanded_vac = expand(deepcopy(kb), p_str)
        if set(str(f) for f in revised_vac) == set(str(f) for f in expanded_vac):
            passed.append("Vacuity")
        else:
            failed.append("Vacuity")

    return passed, failed

# Run postulate tests when script is executed
if __name__ == "__main__":
    passed, failed = test_agm_postulates()
    print("Passed:", passed)
    print("Failed:", failed)
