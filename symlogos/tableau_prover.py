from __future__ import annotations
from typing import Optional

from symlogos.first_order_rules import AlphaRule, DeltaRule, GammaRule
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

        # Pass the signed formula to your tableau expansion methods and proceed with the tableau method
        result = self.tableau_expansion(negated_conclusion)

        return result

    def tableau_expansion(self, signed_formula, depth=0, max_depth=1000):
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
            rule = AlphaRule(signed_formula)
            new_signed_formulas = rule.apply()
        elif isinstance(formula, Forall) or isinstance(formula, Exists):
            if signed_formula.sign == "T" and isinstance(formula, Forall) or signed_formula.sign == "F" and isinstance(formula, Exists):
                rule = GammaRule(signed_formula)
            else:
                rule = DeltaRule(signed_formula)
            new_signed_formulas = [child.signed_formula for child in rule.apply(node)]
        # Add new cases for Necessity and Possibility
        elif isinstance(formula, Necessity):
            if signed_formula.sign == "T":
                rule = ModalBoxTRule(signed_formula)
            else:
                rule = ModalBoxFRule(signed_formula)
            new_signed_formulas = rule.apply()
        elif isinstance(formula, Possibility):
            if signed_formula.sign == "T":
                rule = ModalDiamondTRule(signed_formula)
            else:
                rule = ModalDiamondFRule(signed_formula)
            new_signed_formulas = rule.apply()
        elif isinstance(formula, Not):
            # Create a new signed formula with the negated sign and the inner formula
            new_sign = "T" if signed_formula.sign == "F" else "F"
            new_signed_formula = SignedFormula(new_sign, formula.expr)  # Use expr attribute here
            new_signed_formulas = [new_signed_formula]
        elif isinstance(formula, Implication):
            if signed_formula.sign == "T":
                # Convert the implication to disjunction (¬A ∨ B) and apply the corresponding rule
                new_formula = Or(Not(formula.antecedent), formula.consequent)
                new_signed_formula = SignedFormula(signed_formula.sign, new_formula)
                new_signed_formulas = [new_signed_formula]
            else:
                # Convert the negated implication to conjunction (A ∧ ¬B) and apply the corresponding rule
                new_formula = And(formula.antecedent, Not(formula.consequent))
                new_signed_formula = SignedFormula("T", new_formula)  # Use "T" since we are negating the implication
                new_signed_formulas = [new_signed_formula]
        elif isinstance(formula, Proposition):
            return False  # Atomic propositions cannot be expanded further
        else:
            raise ValueError(f"Unsupported formula type: {type(formula).__name__}")
        
        # Debug: Print the new signed formulas generated
        print(f"New signed formulas: {new_signed_formulas}")

        results = [self.tableau_expansion(new_signed_formula, depth + 1, max_depth) for new_signed_formula in new_signed_formulas]
        return any(results)

    def _is_tableau_closed(self, node):
        signed_formula = node.signed_formula
        opposite_sign = "T" if signed_formula.sign == "F" else "F"
        opposite_signed_formula = SignedFormula(opposite_sign, signed_formula.formula)
        return opposite_signed_formula in self.tableau_formulas
