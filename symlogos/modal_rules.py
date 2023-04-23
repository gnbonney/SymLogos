from symlogos.signed_formula import SignedFormula
from symlogos.modal_operators import Necessity, Possibility
from symlogos.rules import TableauRule

class ModalBoxTRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def apply(self) -> list:
        if not isinstance(self.signed_formula.formula, Necessity) or self.signed_formula.sign != "T":
            raise ValueError("Invalid signed formula for ModalBoxTRule")
        new_signed_formula = SignedFormula("T", self.signed_formula.formula.expr)
        return [new_signed_formula]

    def is_applicable(self) -> bool:
        return self.signed_formula.sign == "T" and isinstance(self.signed_formula.formula, Necessity)

class ModalBoxFRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def apply(self) -> list:
        if not isinstance(self.signed_formula.formula, Necessity) or self.signed_formula.sign != "F":
            raise ValueError("Invalid signed formula for ModalBoxFRule")
        new_signed_formula = SignedFormula("F", self.signed_formula.formula.expr)
        return [new_signed_formula]

    def is_applicable(self) -> bool:
        return self.signed_formula.sign == "F" and isinstance(self.signed_formula.formula, Necessity)

class ModalDiamondTRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def apply(self) -> list:
        if not isinstance(self.signed_formula.formula, Possibility) or self.signed_formula.sign != "T":
            raise ValueError("Invalid signed formula for ModalDiamondTRule")
        new_signed_formula = SignedFormula("T", self.signed_formula.formula.expr)
        return [new_signed_formula]

    def is_applicable(self) -> bool:
        return self.signed_formula.sign == "T" and isinstance(self.signed_formula.formula, Possibility)

class ModalDiamondFRule(TableauRule):
    def __init__(self, signed_formula: SignedFormula) -> None:
        super().__init__(signed_formula)

    def apply(self) -> list:
        if not isinstance(self.signed_formula.formula, Possibility) or self.signed_formula.sign != "F":
            raise ValueError("Invalid signed formula for ModalDiamondFRule")
        new_signed_formula = SignedFormula("F", self.signed_formula.formula.expr)
        return [new_signed_formula]

    def is_applicable(self) -> bool:
        return self.signed_formula.sign == "F" and isinstance(self.signed_formula.formula, Possibility)

