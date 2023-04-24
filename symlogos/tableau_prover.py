from __future__ import annotations
from typing import Optional

from symlogos.first_order_rules import AlphaRule, BetaRule, DeltaRule, GammaRule
from symlogos.modal_operators import Necessity, Possibility
from symlogos.proposition import Proposition
from symlogos.tableau_node import TableauNode
from .signed_formula import SignedFormula
from .connectives import And, Or, Not, Implication
from .quantifiers import Forall, Exists
from symlogos.signed_formula import SignedFormula
from symlogos.modal_rules import ModalBoxTRule, ModalBoxFRule, ModalDiamondTRule, ModalDiamondFRule

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

        # Print statements for debugging
        print("Premises:", premises)
        print("Conclusion:", conclusion)
        print("Negated Conclusion:", negated_conclusion)
        print("Tableau Formulas:", self.tableau_formulas)

        # Pass the signed formula to your tableau expansion methods and proceed with the tableau method
        initial_node = TableauNode(negated_conclusion)
        result = self.tableau_expansion(initial_node)

        return result

    def _handle_and_or(self, signed_formula):
        formula = signed_formula.formula

        if isinstance(formula, Implication):
            if signed_formula.sign == "T":
                return [SignedFormula("F", formula.left), SignedFormula("T", formula.right)]
            else:
                return [SignedFormula("T", formula.left), SignedFormula("F", formula.right)]
        elif isinstance(formula, Not) and isinstance(formula.inner, Implication):
            inner_formula = formula.inner
            if signed_formula.sign == "T":
                return [SignedFormula("T", inner_formula.left), SignedFormula("F", inner_formula.right)]
            else:
                return [SignedFormula("F", inner_formula.left), SignedFormula("T", inner_formula.right)]
        else:
            rule = AlphaRule(signed_formula)
            return rule.apply()

    def _handle_quantifiers(self, node, signed_formula):
        if signed_formula.sign == "T" and isinstance(signed_formula.formula, Forall) or signed_formula.sign == "F" and isinstance(signed_formula.formula, Exists):
            rule = GammaRule(signed_formula)
        else:
            rule = DeltaRule(signed_formula)
        return [child.signed_formula for child in rule.apply(node)]

    def _handle_modal_operators(self, signed_formula):
        formula = signed_formula.formula
        if isinstance(formula, Necessity):
            rule = ModalBoxTRule(signed_formula) if signed_formula.sign == "T" else ModalBoxFRule(signed_formula)
        else:  # isinstance(formula, Possibility)
            rule = ModalDiamondTRule(signed_formula) if signed_formula.sign == "T" else ModalDiamondFRule(signed_formula)
        return rule.apply()

    def _handle_not(self, signed_formula):
        formula = signed_formula.formula
        new_sign = "T" if signed_formula.sign == "F" else "F"
        new_signed_formula = SignedFormula(new_sign, formula.expr)
        return [new_signed_formula]

    def tableau_expansion(self, signed_formula, depth=0, max_depth=1000):
        print(f"Depth: {depth}, Current signed formula: {signed_formula}")
        node = TableauNode(signed_formula)
        self.tableau_formulas.add(node)

        # Debug: Print the current signed formula and depth
        print(f"Depth: {depth}, Current signed formula: {signed_formula}")

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
            new_signed_formulas = self._handle_and_or(signed_formula)
        elif isinstance(formula, Forall) or isinstance(formula, Exists):
            new_signed_formulas = self._handle_quantifiers(node, signed_formula)
        elif isinstance(formula, Necessity) or isinstance(formula, Possibility):
            new_signed_formulas = self._handle_modal_operators(signed_formula)
        elif isinstance(formula, Not):
            new_signed_formulas = self._handle_not(signed_formula)
        else:
            new_signed_formulas = []

        # Debug: Print the new signed formulas generated
        print(f"New signed formulas: {new_signed_formulas}")

        results = [self.tableau_expansion(new_signed_formula, depth + 1, max_depth) for new_signed_formula in new_signed_formulas]
        return any(results)

    def _is_tableau_closed(self, node):
        signed_formula = node.signed_formula
        print(f"Checking closure for: {signed_formula}")

        opposite_sign = "T" if signed_formula.sign == "F" else "F"
        opposite_signed_formula = SignedFormula(opposite_sign, signed_formula.formula)

        for ancestor in node.get_ancestors():
            if ancestor.signed_formula == opposite_signed_formula:
                return True
        return False

