from belief_base import Belief_base

A = Belief_base(["p","p->q"])
A.contract("p")
print(A)

C = Belief_base(["p","p->q"])
C.expand("q")
print(C)
C.revise("!p")
print(C)

B = Belief_base(["p","p->q"])
B.expand("!q<->s")
B.expand("s -> p")
print(B)
B.revise("s")
print(B)