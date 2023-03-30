from .expressions_and_terms import Expression
from .connectives import Not
from .modal_operators import Possibility, Necessity

class Proposition(Expression):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Proposition):
            return self.name == other.name
        return False        

    def __hash__(self):
        return hash((type(self), self.name))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Proposition('{self.name}')"

    def not_(self):
        return Not(self)

    def box(self):
        return Necessity(self)

    def diamond(self):
        return Possibility(self)

    def substitute(self, variable, replacement):
        if self == variable:
            return replacement
        else:
            return self

    def substitute_all_terms(self, term_replacement_dict):
        return self

    def evaluate(self, assignment):
        if self.name in assignment:
            return assignment[self.name]
        else:
            raise ValueError(f"Assignment for proposition '{self.name}' not found.")

    def match(self, other):
        if isinstance(other, Proposition) and self.name == other.name:
            print(f"Proposition match: self: {self}, other: {other}")
            return {}
        else:
            return None
