import unittest
from resolution import entails, revise

class TestBeliefRevision(unittest.TestCase):

    def test_entails_true(self):
        kb = ["p", "p -> q"]
        self.assertTrue(entails(kb, "q"))

    def test_entails_false(self):
        kb = ["p -> q"]
        self.assertFalse(entails(kb, "q"))

    def test_revision_adds_when_not_entailed(self):
        kb = ["p"]
        revised = revise(kb, "!q") # Expected: ["p", "!q"]
        self.assertIn("p", revised)
        self.assertIn("!q", revised)

    def test_revision_no_change_if_already_entailed(self):
        kb = ["p", "p -> q"]
        revised = revise(kb, "q") # Expected: ["p", "p -> q"]
        self.assertEqual(set(revised), set(kb))

    def test_revision_removes_conflict(self):
        kb = ["p", "p -> q"]
        revised = revise(kb, "!q") # Expected: ["p -> q", "!q"] or ["p", "!q"]
        self.assertIn("!q", revised)
        self.assertTrue("p" not in revised or "p -> q" not in revised)
        self.assertTrue("p" in revised or "p -> q" in revised)

    def test_tautologies(self):
        kb = ["p", "!p"]
        self.assertTrue(entails(kb, "q")) # This is true because there is a contradiction in the kb. Logic has broken down everything follows

    def test_entails_tautology_clause_ignored(self):
        kb = ["p", "q", "p | !p"]
        self.assertTrue(entails(kb, "p"))  # tautology doesn't matter

    def test_entails_simple_tautology_not_triggered(self):
        kb = ["p | !p"]  # always true
        self.assertFalse(entails(kb, "q"))  # q is unrelated

if __name__ == "__main__":
    unittest.main()
