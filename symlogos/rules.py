from abc import ABC, abstractmethod
from symlogos.expressions_and_terms import LogicalExpression
from sympy.core.basic import Basic
from typing import List

from symlogos.signed_formula import SignedFormula

class Rule:
    def __init__(self, name: str, premises: List[Basic], conclusion: Basic) -> None:
        self.name = name
        self.premises = premises
        self.conclusion = conclusion

    def __str__(self) -> str:
        premises_str = ", ".join(map(str, self.premises))
        return f"{self.name}: {premises_str} ⊢ {self.conclusion}"

    def __repr__(self) -> str:
        premises_repr = ", ".join(map(repr, self.premises))
        return f"Rule('{self.name}', [{premises_repr}], {repr(self.conclusion)})"

    def apply(self, *args) -> LogicalExpression:
        if len(args) != len(self.premises):
            raise ValueError("Wrong number of arguments")

        match_dicts = []
        for premise, arg in zip(self.premises, args):
            current_match = premise.match(arg)
            print(f"Matching {premise} with {arg}: {current_match}")  # Debug print
            if current_match is None:
                return None
            match_dicts.append(current_match)

        match_dict = {}
        for d in match_dicts:
            match_dict.update(d)

        result = self.conclusion.substitute_all_terms(match_dict)
        print(f"Rule applied: {result}")  # Debug print
        return result

    def to_nnf(self) -> "Rule":
        nnf_premises = [premise.to_nnf() for premise in self.premises]
        nnf_conclusion = self.conclusion.to_nnf()
        return Rule(self.name, nnf_premises, nnf_conclusion)

def check_consistency():
    pass

def check_validity():
    pass

class TableauRule(ABC):

    def __init__(self, signed_formula: SignedFormula) -> None:
        self.signed_formula = signed_formula

    @abstractmethod
    def is_applicable(self):
        """
        Check if the rule is applicable to the signed_formula.
        """
        pass

    @abstractmethod
    def apply(self):
        """
        Apply the rule to the signed_formula and return a list of branches,
        where each branch is a list of SignedFormulas.
        """
        pass