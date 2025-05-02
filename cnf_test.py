import unittest

from ast_nodes import *
from cnf_conversion import *
from parser_test import parse_expr

class TestCNFConversion(unittest.TestCase):
    def test_eliminate_iff(self):
        # (p <-> q) => (p -> q) & (q -> p)
        expr = parse_expr("p <-> q")
        result = eliminate_iff(expr)
        self.assertIsInstance(result, And)
        self.assertIsInstance(result.left, Implies)
        self.assertIsInstance(result.right, Implies)

    def test_eliminate_implies(self):
        # (p -> q) => (!p | q)
        expr = parse_expr("p -> q")
        result = eliminate_implies(expr)
        self.assertIsInstance(result, Or)
        self.assertIsInstance(result.left, Not)
        self.assertIsInstance(result.right, Var)
        self.assertEqual(result.right.name, "q")

    def test_push_not_simple(self):
        # !(p & q) => !p | !q
        expr = parse_expr("!(p & q)")
        no_implies = eliminate_implies(eliminate_iff(expr))
        pushed = push_not(no_implies)
        self.assertIsInstance(pushed, Or)
        self.assertIsInstance(pushed.left, Not)
        self.assertIsInstance(pushed.right, Not)

    def test_double_negation(self):
        # !!p => p
        expr = parse_expr("!!p")
        no_not = simplify_nots(expr)
        self.assertIsInstance(no_not, Var)
        self.assertEqual(no_not.name, "p")

    def test_distribute_or_over_and(self):
        # p | (q & r) => (p | q) & (p | r)
        expr = parse_expr("p | (q & r)")
        no_implies = eliminate_implies(eliminate_iff(expr))
        pushed = push_not(no_implies)
        simplified = simplify_nots(pushed)
        distributed = distribute_or_over_and(simplified)
        self.assertIsInstance(distributed, And)
        self.assertIsInstance(distributed.left, Or)
        self.assertIsInstance(distributed.right, Or)

        # Check structure of left/right
        self.assertEqual(distributed.left.left.name, "p")
        self.assertEqual(distributed.left.right.name, "q")
        self.assertEqual(distributed.right.left.name, "p")
        self.assertEqual(distributed.right.right.name, "r")


    def test_full_to_cnf(self):
        # (p -> q) <-> !(r & s) => (!r | !s | p) & (!r | !s | !q) & (!p | q | r) & (!p | q | s)
        expr = parse_expr("(p -> q) <-> !(r & s)")
        cnf = to_cnf(expr)
        clauses = cnf_to_clauses(cnf)
        expected = [
            ["!r", "!s", "p"],
            ["!r", "!s", "!q"],
            ["!p", "q", "r"],
            ["!p", "q", "s"]
        ]
        self.assertEqual(sorted([sorted(cl) for cl in clauses]), sorted([sorted(cl) for cl in expected]))

if __name__ == "__main__":
    unittest.main()