import unittest
from mastermind import *

class TestMastermind(unittest.TestCase):

    def test_1(self):
        goal = (0, 0)
        amount_of_pegs = 2
        amount_of_colors = 2
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

    def test_2(self):
        goal = (0, 1)
        amount_of_pegs = 2
        amount_of_colors = 2
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

    def test_3(self):
        goal = (1, 0)
        amount_of_pegs = 2
        amount_of_colors = 2
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

    def test_4(self):
        goal = (1, 1)
        amount_of_pegs = 2
        amount_of_colors = 2
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

    def test_5(self):
        goal = (0, 0)
        amount_of_pegs = 2
        amount_of_colors = 3
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

    def test_6(self):
        goal = (0, 1)
        amount_of_pegs = 2
        amount_of_colors = 3
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

    def test_7(self):
        goal = (1, 0)
        amount_of_pegs = 2
        amount_of_colors = 3
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

    def test_8(self):
        goal = (1, 1)
        amount_of_pegs = 2
        amount_of_colors = 3
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

    def test_9(self):
        goal = (1, 1)
        amount_of_pegs = 2
        amount_of_colors = 4
        kb = generate_kb(amount_of_pegs, amount_of_colors)
        result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
        self.assertEqual(goal, result)

if __name__ == "__main__":
    unittest.main()




