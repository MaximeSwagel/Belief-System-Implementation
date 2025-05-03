import unittest
from contraction import contract
from resolution import entails

class TestBeliefContraction(unittest.TestCase):

    def test_basic_contraction(self):
        kb = ["p", "p -> q"]
        contracted = contract(kb, "q") # Expected: either ["p"] or ["p -> q"] or []
        self.assertFalse(entails(contracted, "q"))
        self.assertIn(set(contracted), [set(["p"]), set(["p -> q"]), set([])])

    def test_basic_contraction_prio(self):
        kb = ["p", "p -> q"]
        contracted = contract(kb, "q") # Expected: ["p"] as it has the highest priority
        self.assertFalse(entails(contracted, "q"))
        self.assertEqual(set(contracted), set(["p"]))

    def test_basic_contraction_prio_2(self):
        kb = ["p -> q", "p"]
        contracted = contract(kb, "q") # Expected: ["p -> q"] as it has the highest priority
        self.assertFalse(entails(contracted, "q"))
        self.assertEqual(set(contracted), set(["p -> q"]))

    def test_no_entailment_no_change(self):
        kb = ["p"]
        contracted = contract(kb, "q") # Nothing should be removed
        self.assertEqual(set(contracted), set(kb))

    def test_contraction_removes_single_belief(self):
        kb = ["q"]
        contracted = contract(kb, "q") # Expected: [] as q is removed
        self.assertEqual(contracted, [])
        self.assertFalse(entails(contracted, "q"))

    def test_contraction_redundant_support_kb(self):
        kb = ["p", "q", "p -> r", "q -> r"]
        contracted = contract(kb, "r")
        # Contract needs to remove both paths to r. Remove ((p) or (p -> r)) and ((q) or (q -> r))
        # With prio expected ["p", "q"]
        self.assertFalse(entails(contracted, "r"))
        self.assertEqual(set(contracted), set(["p", "q"]))

    def test_contraction_chain_implication(self):
        kb = ["p -> q", "p", "q -> r", "r -> s"]
        contracted = contract(kb, "s") # Expected: ["p", "q -> r", "r -> s"] or ["p -> q", "p", "r -> s"] or ["p -> q", "p", "q -> r"]
        self.assertFalse(entails(contracted, "s"))

    def test_contraction_empty_kb(self):
        kb = []
        contracted = contract(kb, "p") # Nothing is remove as there is nothing
        self.assertEqual(contracted, [])

if __name__ == "__main__":
    unittest.main()
