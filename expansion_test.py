import unittest
from expansion import expand, parse

class TestExpansion(unittest.TestCase):
    def test_adds_new_belief(self):
        kb = ["p"]
        self.assertEqual(set(expand(kb, "q")), {"p", "q"})

    def test_ignores_duplicates(self):
        kb = ["p"]
        self.assertEqual(expand(kb, "p"), ["p"])

if __name__ == "__main__":
    unittest.main()