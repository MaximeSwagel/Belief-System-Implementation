# Mastemind
New plan without filters and pure logical inference

- The secret code with 2 pegs
- Colors: Red (R), Green (G), Blue (B), Yellow (Y)

Repetition is allowed, so there is 4x4=16 possible combinations.

# Step 0 initial belief state
kb = [
    (p1_R | p1_G | p1_B | p1_Y),
    !(p1_R & p1_G),
    !(p1_R & p1_B),
    !(p1_R & p1_Y),
    !(p1_G & p1_B),
    !(p1_G & p1_Y),
    !(p1_B & p1_Y),
    (p2_R | p2_G | p2_B | p2_Y),
    !(p2_R & p2_G),
    !(p2_R & p2_B),
    !(p2_R & p2_Y),
    !(p2_G & p2_B),
    !(p2_G & p2_Y),
    !(p2_B & p2_Y)
]

# First guess
Guess = (R, G)
Aka (p1_R & p2_G)

feedback 1 white peg
(p1_G | p2_R) & !p1_R & !p2_G


Revise belief base
Revise(kb, feedback)
    Contract kb by !(feedback)
    Expand kb by feedback

# repeat until one solution left
