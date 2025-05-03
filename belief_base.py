from contraction import contract
from expansion import expand
from revision import revise

class Belief_base:
    def __init__(self,Kb :list[str]):
        self.beliefs = Kb
    
    def contract(self,formula : str):
        contract(self.Kb,formula)

    def expand(self,formula : str):
        expand(self.Kb,formula)

    def resolve(self,formula :str):
        revise(self.Kb,formula)