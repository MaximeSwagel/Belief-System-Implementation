from ast_nodes import *

def to_cnf(expr: Expr) -> Expr:
    expr = eliminate_iff(expr)
    expr = eliminate_implies(expr)
    expr = push_not(expr)
    expr = simplify_nots(expr)
    expr = distribute_or_over_and(expr)
    return expr

def eliminate_iff(expr: Expr) -> Expr:
    if isinstance(expr, Var):
        return expr
    elif isinstance(expr, Not):
        return Not(eliminate_iff(expr.expr))
    elif isinstance(expr, And):
        return And(eliminate_iff(expr.left), eliminate_iff(expr.right))
    elif isinstance(expr, Or):
        return Or(eliminate_iff(expr.left), eliminate_iff(expr.right))
    elif isinstance(expr, Implies):
        return Implies(eliminate_iff(expr.left), eliminate_iff(expr.right))
    elif isinstance(expr, Iff):
        # p <-> q  ==>  (p -> q) & (q -> p)
        left = eliminate_iff(expr.left)
        right = eliminate_iff(expr.right)
        return And(Implies(left, right), Implies(right, left))

def eliminate_implies(expr: Expr) -> Expr:
    if isinstance(expr, Var):
        return expr
    elif isinstance(expr, Not):
        return Not(eliminate_implies(expr.expr))
    elif isinstance(expr, And):
        return And(eliminate_implies(expr.left), eliminate_implies(expr.right))
    elif isinstance(expr, Or):
        return Or(eliminate_implies(expr.left), eliminate_implies(expr.right))
    elif isinstance(expr, Implies):
        # p -> q  ⇒  !p | q
        left = eliminate_implies(expr.left)
        right = eliminate_implies(expr.right)
        return Or(Not(left), right)

def push_not(expr: Expr) -> Expr:
    if isinstance(expr, Var):
        return expr
    elif isinstance(expr, Not):
        inner = expr.expr
        if isinstance(inner, Var):
            return expr  # !p
        elif isinstance(inner, Not):
            return push_not(inner.expr)  # !!p ⇒ p
        elif isinstance(inner, And):
            # !(A & B) ⇒ !A | !B
            return Or(push_not(Not(inner.left)), push_not(Not(inner.right)))
        elif isinstance(inner, Or):
            # !(A | B) ⇒ !A & !B
            return And(push_not(Not(inner.left)), push_not(Not(inner.right)))
        else:
            raise TypeError(f"Unexpected NOT operand: {type(inner)}")
    elif isinstance(expr, And):
        return And(push_not(expr.left), push_not(expr.right))
    elif isinstance(expr, Or):
        return Or(push_not(expr.left), push_not(expr.right))

def simplify_nots(expr: Expr) -> Expr:
    if isinstance(expr, Var):
        return expr
    elif isinstance(expr, Not):
        inner = simplify_nots(expr.expr)
        if isinstance(inner, Not):
            return simplify_nots(inner.expr)
        return Not(inner)
    elif isinstance(expr, And):
        return And(simplify_nots(expr.left), simplify_nots(expr.right))
    elif isinstance(expr, Or):
        return Or(simplify_nots(expr.left), simplify_nots(expr.right))

def distribute_or_over_and(expr: Expr) -> Expr:
    if isinstance(expr, Var) or isinstance(expr, Not):
        return expr
    elif isinstance(expr, And):
        return And(
            distribute_or_over_and(expr.left),
            distribute_or_over_and(expr.right)
        )
    elif isinstance(expr, Or):
        left = distribute_or_over_and(expr.left)
        right = distribute_or_over_and(expr.right)
        # Apply distributive law if needed
        if isinstance(left, And):
            # (A & B) | C ⇒ (A | C) & (B | C)
            return And(
                distribute_or_over_and(Or(left.left, right)),
                distribute_or_over_and(Or(left.right, right))
            )
        elif isinstance(right, And):
            # A | (B & C) ⇒ (A | B) & (A | C)
            return And(
                distribute_or_over_and(Or(left, right.left)),
                distribute_or_over_and(Or(left, right.right))
            )
        else:
            return Or(left, right)


def flatten_and(expr: Expr) -> list[Expr]:
    if isinstance(expr, And):
        return flatten_and(expr.left) + flatten_and(expr.right)
    else:
        return [expr]

def flatten_or(expr: Expr) -> list[Expr]:
    if isinstance(expr, Or):
        return flatten_or(expr.left) + flatten_or(expr.right)
    else:
        return [expr]
    
def literal_to_str(expr: Expr) -> str:
    if isinstance(expr, Var):
        return expr.name
    elif isinstance(expr, Not) and isinstance(expr.expr, Var):
        return f'!{expr.expr.name}'
    else:
        raise ValueError(f"Unexpected literal: {expr}")

def cnf_to_clauses(expr: Expr) -> list[list[str]]:
    and_parts = flatten_and(expr)
    clauses = []
    for part in and_parts:
        or_parts = flatten_or(part)
        literals = [literal_to_str(lit) for lit in or_parts]
        clauses.append(sorted(set(literals)))
    return clauses