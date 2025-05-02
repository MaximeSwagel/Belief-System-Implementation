from parser_test import parse_expr
from parser import Parser
from tokenizer import tokenize

def _str_eq(f1, f2):
    """Two formulas are equal if their printed concrete syntax is equal."""
    return str(f1) == str(f2)

# Helper to parse logic strings into AST
def parse(s):
    return Parser(tokenize(s)).parse()

def expand(kb, phi_str) -> list:
    """
    Parameters
    ----------
    kb       list[str | ast_nodes.Expr]   belief base (strings *or* ASTs)
    phi_str  str                         sentence to be added

    Returns
    -------
    list      new belief base (shallow copy)
    """
    # Keep the KB representation uniform: everything as strings
    kb_strings = [str(f) for f in kb]
    phi = parse(phi_str)
    for kb_str in kb_strings:
        if _str_eq(phi_str, kb_str):
            return kb               # nothing to add

    kb.append(phi_str)
    return kb