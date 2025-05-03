from belief_base import Belief_base

Kb = [
    "(p1_R | p1_G | p1_B | p1_Y)",
    "!(p1_R & p1_G)",
    "!(p1_R & p1_B)",
    "!(p1_R & p1_Y)",
    "!(p1_G & p1_B)",
    "!(p1_G & p1_Y)",
    "!(p1_B & p1_Y)",
    "(p2_R | p2_G | p2_B | p2_Y)",
    "!(p2_R & p2_G)",
    "!(p2_R & p2_B)",
    "!(p2_R & p2_Y)",
    "!(p2_G & p2_B)",
    "!(p2_G & p2_Y)",
    "!(p2_B & p2_Y)"]

A = Belief_base(Kb)

#first gess