from symlogos.connectives import And, Implication, Or
from symlogos.expressions_and_terms import Term
from symlogos.quantifiers import Exists, Forall
from symlogos.rules import TableauRule
from symlogos.signed_formula import SignedFormula
from typing import List

from symlogos.tableau_node import TableauNode


class AlphaRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def __hash__(self):
        return hash((type(self), self.signed_formula))

    def is_applicable(self) -> bool:
        formula = self.signed_formula.formula
        return isinstance(formula, And) or isinstance(formula, Or)

    def apply(self) -> List[SignedFormula]:
        print(f"AlphaRule: Applying rule to {self.signed_formula}")
        if not self.is_applicable():
            raise ValueError("Alpha rule is not applicable to the given formula")

        formula = self.signed_formula.formula
        left = formula.left
        right = formula.right

        if isinstance(formula, And):
            if self.signed_formula.is_positive():
                result = [SignedFormula('T', left), SignedFormula('T', right)]
            else:
                result = [SignedFormula('F', left), SignedFormula('F', right)]
        elif isinstance(formula, Or):
            if self.signed_formula.is_positive():
                result = [SignedFormula('T', left), SignedFormula('T', right)]
            else:
                result = [SignedFormula('F', left), SignedFormula('F', right)]
        print(f"AlphaRule: Result: {result}")
        return result

class BetaRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def __hash__(self):
        return hash((type(self), self.signed_formula))

    def is_applicable(self) -> bool:
        formula = self.signed_formula.formula
        return isinstance(formula, Implication)

    def apply(self) -> List[SignedFormula]:
        if not self.is_applicable():
            raise ValueError("Beta rule is not applicable to the given formula")

        formula = self.signed_formula.formula

        if isinstance(formula, Implication):
            antecedent = formula.antecedent
            consequent = formula.consequent

            if self.signed_formula.is_positive():
                return [SignedFormula('F', antecedent), SignedFormula('T', consequent)]
            else:
                return [SignedFormula('T', antecedent), SignedFormula('F', consequent)]

class GammaRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def __hash__(self):
        return hash((type(self), self.signed_formula))

    def is_applicable(self) -> bool:
        return isinstance(self.signed_formula.formula, Exists) and self.signed_formula.sign == "F"

    def apply(self, node: TableauNode) -> List[TableauNode]:
        print(f"{self.__class__.__name__}: Applying rule to {self.signed_formula}")
        quantifier_formula = self.signed_formula.formula
        if not self.is_applicable():
            raise ValueError("GammaRule can only be applied to negated Exists quantifiers")

        fresh_variable = Term("v_" + str(node.get_next_fresh_variable_index()))
        instantiated_formula = quantifier_formula.predicate.substitute({quantifier_formula.variable: fresh_variable})
        new_node = TableauNode(SignedFormula("T", instantiated_formula), node)
        node.children.append(new_node)
        result = [new_node]
        print(f"{self.__class__.__name__}: Result: {result}")
        return result


class DeltaRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def __hash__(self):
        return hash((type(self), self.signed_formula))

    def is_applicable(self):
        return isinstance(self.signed_formula.formula, Forall)

    def apply(self, node: TableauNode) -> List[TableauNode]:
        quantifier_formula = self.signed_formula.formula
        if not (isinstance(quantifier_formula, Forall) and self.signed_formula.sign == "F"):
            raise ValueError("DeltaRule can only be applied to negated Forall quantifiers")

        fresh_variable = Term("v_" + str(node.get_next_fresh_variable_index()))
        instantiated_formula = quantifier_formula.predicate.substitute({quantifier_formula.variable: fresh_variable})
        new_node = TableauNode(SignedFormula("T", instantiated_formula), node)
        node.children.append(new_node)
        result = [new_node]
        print(f"{self.__class__.__name__}: Result: {result}")
        return result