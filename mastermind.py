from revision import revise
from resolution import entails
from itertools import product

def get_remaining_candidates(kb, pegs, colors):
    all_codes = product(range(colors), repeat=pegs)
    return [code for code in all_codes if is_consistent(kb, encode_guess(code))]

def generate_kb(pegs, colors):
    kb = []
    for i in range(pegs):
        kb.append(" | ".join(f"p{i}_c{c}" for c in range(colors)))
        for c1 in range(colors):
            for c2 in range(c1 + 1, colors):
                kb.append(f"!(p{i}_c{c1} & p{i}_c{c2})")
    return kb

def encode_guess(guess):
    return " & ".join(f"p{i}_c{c}" for i, c in enumerate(guess))

def get_feedback(guess, goal):
    black = sum(g == a for g, a in zip(guess, goal))
    guess_count = {c: guess.count(c) for c in set(guess)}
    goal_count = {c: goal.count(c) for c in set(goal)}
    shared = sum(min(guess_count.get(k, 0), goal_count.get(k, 0)) for k in guess_count)
    white = shared - black
    return black, white

def feedback_to_formula(guess, feedback):
    black, white = feedback
    terms = [f"p{i}_c{c}" for i, c in enumerate(guess)]
    if (black, white) == (2, 0):
        return " & ".join(terms)
    if (black, white) == (1, 0):
        return f"({' | '.join(terms)}) & !({' & '.join(terms)})"
    if (black, white) == (0, 0):
        return " & ".join(f"!{t}" for t in terms)
    if (black, white) == (0, 1):
        wrong_places = [f"!p{i}_c{c}" for i, c in enumerate(guess)]
        others = [f"p{(i+1)%len(guess)}_c{c}" for i, c in enumerate(guess)]
        return f"({' | '.join(others)}) & {' & '.join(wrong_places)}"
    if (black, white) == (0, 2):
        wrong_pos = [f"!p{idx}_c{c}" for idx, c in enumerate(guess)]
        flipped = [f"p{(idx + 1) % len(guess)}_c{c}" for idx, c in enumerate(guess)]
        return f"({' & '.join(flipped)}) & {' & '.join(wrong_pos)}"
    return f"({' | '.join(terms)})"

def mastermind(kb, goal, pegs, colors):
    round = 1
    while True:
        candidates = get_remaining_candidates(kb, pegs, colors)
        print(f'Candidates {candidates}')
        guess = candidates[0]
        print(f'Guess {guess}')

        if len(candidates) == 1:
            return guess

        feedback = get_feedback(guess, goal)
        print(f'Feedback {feedback}')

        if feedback[0] == pegs:
            return guess

        formula = feedback_to_formula(guess, feedback)
        print(f'Formula {formula}')
        kb = revise(kb, formula)
        print(f'kb {round}: {kb}')
        round += 1


def is_consistent(kb, formula):
    return not entails(kb, f"!({formula})")

def main():
    goal = (1, 1)
    amount_of_pegs = 2
    amount_of_colors = 3
    kb = generate_kb(amount_of_pegs, amount_of_colors)
    print(f"Initial KB: {kb}")


    result = mastermind(kb, goal, amount_of_pegs, amount_of_colors)
    if result == goal:
        print("Success!")
    else:
        print("Failed. Final guess:", result)

if __name__ == "__main__":
    main()



"""
goal = (0, 0)
amount_of_pegs = 2
amount_of_colors = 2

Initial KB: ['p0_c0 | p0_c1', '!(p0_c0 & p0_c1)', 'p1_c0 | p1_c1', '!(p1_c0 & p1_c1)']
Candidates [(0, 0), (0, 1), (1, 0), (1, 1)]
Guess (0, 0)
Feedback (2, 0)
Success!
"""


"""
goal = (0, 1)
amount_of_pegs = 2
amount_of_colors = 2

Initial KB: ['p0_c0 | p0_c1', '!(p0_c0 & p0_c1)', 'p1_c0 | p1_c1', '!(p1_c0 & p1_c1)']
Candidates [(0, 0), (0, 1), (1, 0), (1, 1)]
Guess (0, 0)
Feedback (1, 0)
Formula (p0_c0 | p1_c0) & !(p0_c0 & p1_c0)
kb 1: ['p0_c0 | p0_c1', '!(p0_c0 & p0_c1)', 'p1_c0 | p1_c1', '!(p1_c0 & p1_c1)', '(p0_c0 | p1_c0) & !(p0_c0 & p1_c0)']
Candidates [(0, 1), (1, 0)]
Guess (0, 1)
Feedback (2, 0)
Success!
"""

"""
goal = (1, 0)
amount_of_pegs = 2
amount_of_colors = 2

Initial KB: ['p0_c0 | p0_c1', '!(p0_c0 & p0_c1)', 'p1_c0 | p1_c1', '!(p1_c0 & p1_c1)']
Candidates [(0, 0), (0, 1), (1, 0), (1, 1)]
Guess (0, 0)
Feedback (1, 0)
Formula (p0_c0 | p1_c0) & !(p0_c0 & p1_c0)
kb 1: ['p0_c0 | p0_c1', '!(p0_c0 & p0_c1)', 'p1_c0 | p1_c1', '!(p1_c0 & p1_c1)', '(p0_c0 | p1_c0) & !(p0_c0 & p1_c0)']
Candidates [(0, 1), (1, 0)]
Guess (0, 1)
Feedback (0, 2)
Formula (p1_c0 & p0_c1) & !p0_c0 & !p1_c1
kb 2: ['p0_c0 | p0_c1', '!(p0_c0 & p0_c1)', 'p1_c0 | p1_c1', '!(p1_c0 & p1_c1)', '(p0_c0 | p1_c0) & !(p0_c0 & p1_c0)', '(p1_c0 & p0_c1) & !p0_c0 & !p1_c1']
Candidates [(1, 0)]
Guess (1, 0)
Success!
"""

"""
goal = (1, 1)
amount_of_pegs = 2
amount_of_colors = 2

Initial KB: ['p0_c0 | p0_c1', '!(p0_c0 & p0_c1)', 'p1_c0 | p1_c1', '!(p1_c0 & p1_c1)']
Candidates [(0, 0), (0, 1), (1, 0), (1, 1)]
Guess (0, 0)
Feedback (0, 0)
Formula !p0_c0 & !p1_c0
kb 1: ['p0_c0 | p0_c1', '!(p0_c0 & p0_c1)', 'p1_c0 | p1_c1', '!(p1_c0 & p1_c1)', '!p0_c0 & !p1_c0']
Candidates [(1, 1)]
Guess (1, 1)
Success!
"""



"""
goal = (1, 1)
amount_of_pegs = 2
amount_of_colors = 3

Initial KB: ['p0_c0 | p0_c1 | p0_c2', '!(p0_c0 & p0_c1)', '!(p0_c0 & p0_c2)', '!(p0_c1 & p0_c2)', 'p1_c0 | p1_c1 | p1_c2', '!(p1_c0 & p1_c1)', '!(p1_c0 & p1_c2)', '!(p1_c1 & p1_c2)']
Candidates [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
Guess (0, 0)
Feedback (0, 0)
Formula !p0_c0 & !p1_c0
kb 1: ['p0_c0 | p0_c1 | p0_c2', '!(p0_c0 & p0_c1)', '!(p0_c0 & p0_c2)', '!(p0_c1 & p0_c2)', 'p1_c0 | p1_c1 | p1_c2', '!(p1_c0 & p1_c1)', '!(p1_c0 & p1_c2)', '!(p1_c1 & p1_c2)', '!p0_c0 & !p1_c0']
Candidates [(1, 1), (1, 2), (2, 1), (2, 2)]
Guess (1, 1)
Feedback (2, 0)
Success!
"""

"""
goal = (1, 1)
amount_of_pegs = 2
amount_of_colors = 4

Initial KB: ['p0_c0 | p0_c1 | p0_c2 | p0_c3', '!(p0_c0 & p0_c1)', '!(p0_c0 & p0_c2)', '!(p0_c0 & p0_c3)', '!(p0_c1 & p0_c2)', '!(p0_c1 & p0_c3)', '!(p0_c2 & p0_c3)', 'p1_c0 | p1_c1 | p1_c2 | p1_c3', '!(p1_c0 & p1_c1)', '!(p1_c0 & p1_c2)', '!(p1_c0 & p1_c3)', '!(p1_c1 & p1_c2)', '!(p1_c1 & p1_c3)', '!(p1_c2 & p1_c3)']
Candidates [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
Guess (0, 0)
Feedback (0, 0)
Formula !p0_c0 & !p1_c0
kb 1: ['p0_c0 | p0_c1 | p0_c2 | p0_c3', '!(p0_c0 & p0_c1)', '!(p0_c0 & p0_c2)', '!(p0_c0 & p0_c3)', '!(p0_c1 & p0_c2)', '!(p0_c1 & p0_c3)', '!(p0_c2 & p0_c3)', 'p1_c0 | p1_c1 | p1_c2 | p1_c3', '!(p1_c0 & p1_c1)', '!(p1_c0 & p1_c2)', '!(p1_c0 & p1_c3)', '!(p1_c1 & p1_c2)', '!(p1_c1 & p1_c3)', '!(p1_c2 & p1_c3)', '!p0_c0 & !p1_c0']
Candidates [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
Guess (1, 1)
Feedback (2, 0)
Success!
"""
