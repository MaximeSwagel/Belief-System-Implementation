from contraction import contract
from expansion import expand
from revision import revise, test_agm_postulates

class Belief_base:
    def __init__(self,Bs :list[str]):
        self.beliefs = Bs
    
    def contract(self,formula : str):
        self.beliefs = contract(self.beliefs,formula)

    def expand(self,formula : str):
        self.beliefs = expand(self.beliefs,formula)

    def revise(self,formula :str):
        self.beliefs = revise(self.beliefs,formula)
    
    def __str__(self):
        return '{' + ','.join(str(belief) for belief in self.beliefs) + '}'