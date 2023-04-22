import pytest
from symlogos.modal_rules import ModalBoxTRule, ModalBoxFRule, ModalDiamondTRule, ModalDiamondFRule
from symlogos.signed_formula import SignedFormula
from symlogos.modal_operators import Necessity, Possibility
from symlogos.proposition import Proposition

@pytest.fixture
def A():
    return Proposition("A")

@pytest.fixture
def B():
    return Proposition("B")

def test_modal_box_t_rule(A):
    signed_formula = SignedFormula("T", Necessity(A))
    rule = ModalBoxTRule(signed_formula)
    new_signed_formulas = rule.apply()

    assert len(new_signed_formulas) == 1
    assert new_signed_formulas[0] == SignedFormula("T", A)

def test_modal_box_f_rule(A):
    signed_formula = SignedFormula("F", Necessity(A))
    rule = ModalBoxFRule(signed_formula)
    new_signed_formulas = rule.apply()

    assert len(new_signed_formulas) == 1
    assert new_signed_formulas[0] == SignedFormula("F", A)

def test_modal_diamond_t_rule(A):
    signed_formula = SignedFormula("T", Possibility(A))
    rule = ModalDiamondTRule(signed_formula)
    new_signed_formulas = rule.apply()

    assert len(new_signed_formulas) == 1
    assert new_signed_formulas[0] == SignedFormula("T", A)

def test_modal_diamond_f_rule(A):
    signed_formula = SignedFormula("F", Possibility(A))
    rule = ModalDiamondFRule(signed_formula)
    new_signed_formulas = rule.apply()

    assert len(new_signed_formulas) == 1
    assert new_signed_formulas[0] == SignedFormula("F", A)
