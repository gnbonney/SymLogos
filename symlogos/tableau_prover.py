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
        # Create a set of signed formulas for the premises with the sign "T"
        tableau_formulas = {SignedFormula("T", premise) for premise in premises}

        # Create a signed formula for the negation of the conclusion with the sign "F"
        negated_conclusion = SignedFormula("F", Not(conclusion))

        # Add the negated conclusion to the tableau formulas
        tableau_formulas.add(negated_conclusion)

        # Print statements for debugging
        print("Premises:", premises)
        print("Conclusion:", conclusion)
        print("Negated Conclusion:", negated_conclusion)
        print("Tableau Formulas:", tableau_formulas)

        # Pass the signed formula to your tableau expansion methods and proceed with the tableau method
        initial_node = TableauNode(negated_conclusion)
        result = self.tableau_expansion(initial_node)

        # Check if the tableau is closed
        return not result


    def _handle_and_or(self, param):
        if isinstance(param, TableauNode):
            formula = param.signed_formula.formula
            signed_formula = param.signed_formula
        elif isinstance(param, SignedFormula):
            formula = param.formula
            signed_formula = param
        else:
            raise ValueError("unexpected input to _handle_and_or")

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
        elif isinstance(formula, And):
            if signed_formula.sign == "T":
                return [SignedFormula("T", formula.left), SignedFormula("T", formula.right)]
            else:
                return [SignedFormula("F", formula.left), SignedFormula("F", formula.right)]
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

    def tableau_expansion(self, node: TableauNode, depth=0, max_depth=1000):
        signed_formula = node.signed_formula

        # Debug: Print the current signed formula and depth
        print(f"Depth: {depth}, Current signed formula: {signed_formula}")

        # Check for termination conditions
        if depth >= max_depth:
            # Maximum depth reached; cannot determine if the tableau is closed
            return False

        # Check if the tableau is closed
        if self._is_tableau_closed(node):
            print(f"Tableau closed at depth {depth} with signed formula {signed_formula}")
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

        results = [self.tableau_expansion(node.add_child(new_signed_formula), depth + 1, max_depth) for new_signed_formula in new_signed_formulas]
        return any(results)

    def _is_tableau_closed(self, node: TableauNode) -> bool:
        signed_formulas = [node.signed_formula] + [ancestor.signed_formula for ancestor in node.get_ancestors()]

        print("Signed formulas in the current branch:")
        for sf in signed_formulas:
            print(sf)

        for sf1 in signed_formulas:
            for sf2 in signed_formulas:
                if sf1.formula == sf2.formula and sf1.sign != sf2.sign:
                    return True

        return False

