from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, List
from .signed_formula import SignedFormula
from .connectives import And, Or, Not, Implication
from .quantifiers import Forall, Exists
from .expressions_and_terms import Term
from symlogos.signed_formula import SignedFormula

class TableauNode:
    def __init__(self, signed_formula: SignedFormula, parent: Optional[TableauNode]=None) -> None:
        self.signed_formula = signed_formula
        self.parent = parent
        self.children = []

    def add_child(self, signed_formula):
        child_node = TableauNode(signed_formula, parent=self)
        self.children.append(child_node)
        return child_node

    def get_next_fresh_constant_index(self):
        if self.parent:
            return self.parent.get_next_fresh_constant_index() + 1
        else:
            return 0

    def get_next_fresh_variable_index(self) -> int:
        if self.parent:
            return self.parent.get_next_fresh_variable_index() + 1
        else:
            return 0

class TableauProver:
    def __init__(self):
        self.tableau_formulas = set()

    def is_sound(self, premises, conclusion):
        # Convert premises and negated conclusion to signed formulas
        def convert_to_signed_formula(formula, sign="T"):
            if isinstance(formula, Implication):
                if sign == "T":
                    # Convert P -> Q to ~P or Q
                    formula = Or(Not(formula.left), formula.right)
                else:
                    # Convert ~(P -> Q) to P and ~Q
                    formula = And(formula.left, Not(formula.right))
            return SignedFormula(sign, formula)

        # Create a set of signed formulas for the premises with the sign "T"
        self.tableau_formulas = {convert_to_signed_formula(premise) for premise in premises}

        # Create a signed formula for the negation of the conclusion with the sign "F"
        negated_conclusion = convert_to_signed_formula(conclusion, sign="F")

        # Add the negated conclusion to the tableau formulas
        self.tableau_formulas.add(negated_conclusion)

        # Pass the signed formula to your tableau expansion methods and proceed with the tableau method
        result = self.tableau_expansion(negated_conclusion)

        return result

    def tableau_expansion(self, signed_formula, depth=0, max_depth=1000):
        node = TableauNode(signed_formula)
        self.tableau_formulas.add(node)

        # Check for termination conditions
        if depth >= max_depth:
            # Maximum depth reached; cannot determine if the tableau is closed
            return False

        # Check if the tableau is closed
        if self._is_tableau_closed(node):
            return True

        # Apply tableau rules to the signed formula
        formula = signed_formula.formula
        if isinstance(formula, And) or isinstance(formula, Or):
            rule = AlphaRule() if isinstance(formula, And) else BetaRule()
        elif isinstance(formula, Forall) or isinstance(formula, Exists):
            if signed_formula.sign == "T" and isinstance(formula, Forall) or signed_formula.sign == "F" and isinstance(formula, Exists):
                rule = GammaRule(signed_formula)
            else:
                rule = DeltaRule(signed_formula)
        else:
            raise ValueError("Unsupported formula type")

        new_signed_formulas = rule.apply(node)
        results = [self.tableau_expansion(new_signed_formula, depth + 1, max_depth) for new_signed_formula in new_signed_formulas]
        return all(results) if isinstance(rule, AlphaRule) else any(results)



    def _is_tableau_closed(self, node):
        signed_formula = node.signed_formula
        opposite_sign = "T" if signed_formula.sign == "F" else "F"
        opposite_signed_formula = SignedFormula(opposite_sign, signed_formula.formula)
        return opposite_signed_formula in self.tableau_formulas



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

class AlphaRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def __hash__(self):
        return hash((type(self), self.signed_formula))

    def is_applicable(self) -> bool:
        formula = self.signed_formula.formula
        return isinstance(formula, And) or isinstance(formula, Or)

    def apply(self) -> List[SignedFormula]:
        if not self.is_applicable():
            raise ValueError("Alpha rule is not applicable to the given formula")

        formula = self.signed_formula.formula
        left = formula.left
        right = formula.right

        if isinstance(formula, And):
            if self.signed_formula.is_positive():
                return [SignedFormula('T', left), SignedFormula('T', right)]
            else:
                return [SignedFormula('F', left), SignedFormula('F', right)]
        elif isinstance(formula, Or):
            if self.signed_formula.is_positive():
                return [SignedFormula('T', left), SignedFormula('T', right)]
            else:
                return [SignedFormula('F', left), SignedFormula('F', right)]


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
        quantifier_formula = self.signed_formula.formula
        if not self.is_applicable():
            raise ValueError("GammaRule can only be applied to negated Exists quantifiers")

        fresh_variable = Term("v_" + str(node.get_next_fresh_variable_index()))
        instantiated_formula = quantifier_formula.predicate.substitute({quantifier_formula.variable: fresh_variable})
        new_node = TableauNode(SignedFormula("T", instantiated_formula), node)
        node.children.append(new_node)
        return [new_node]


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
        return [new_node]


