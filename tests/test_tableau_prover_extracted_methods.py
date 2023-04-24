import pytest
from symlogos.expressions_and_terms import Term
from symlogos.functions_and_predicates import Predicate
from symlogos.tableau_node import TableauNode
from symlogos.tableau_prover import TableauProver
from symlogos.signed_formula import SignedFormula
from symlogos.connectives import And, Or, Not
from symlogos.quantifiers import Forall, Exists
from symlogos.proposition import Proposition
from symlogos.modal_operators import Necessity, Possibility

@pytest.fixture
def tableau_prover():
    return TableauProver()

def test_handle_and_or(tableau_prover):
    A = Proposition("A")
    B = Proposition("B")

    signed_formula_and = SignedFormula("T", And(A, B))
    signed_formula_or = SignedFormula("F", Or(A, B))

    new_signed_formulas_and = tableau_prover._handle_and_or(signed_formula_and)
    new_signed_formulas_or = tableau_prover._handle_and_or(signed_formula_or)

    # Assertions for And
    assert len(new_signed_formulas_and) == 2
    assert all(sf.sign == "T" for sf in new_signed_formulas_and)
    assert {sf.formula for sf in new_signed_formulas_and} == {A, B}

    # Assertions for Or
    assert len(new_signed_formulas_or) == 2
    assert all(sf.sign == "F" for sf in new_signed_formulas_or)
    assert {sf.formula for sf in new_signed_formulas_or} == {A, B}

def test_handle_quantifiers(tableau_prover):
    P = Predicate("P")
    x = Term("x")
    Px = Predicate("P", x)
    signed_formula_exists = SignedFormula("F", Exists(x, Px))

    signed_formula_example = SignedFormula("T", Px)
    node = TableauNode(signed_formula_example)

    new_signed_formulas_exists = tableau_prover._handle_quantifiers(node, signed_formula_exists)

    # Assertions for negated Exists quantifier
    assert len(new_signed_formulas_exists) == 1
    assert new_signed_formulas_exists[0].sign == "T"  
    assert isinstance(new_signed_formulas_exists[0].formula, Predicate)
    assert str(new_signed_formulas_exists[0].formula.symbol) == "P"  # This line is updated


def test_handle_modal_operators(tableau_prover):
    A = Proposition("A")

    signed_formula_box_t = SignedFormula("T", Necessity(A))
    signed_formula_box_f = SignedFormula("F", Necessity(A))
    signed_formula_diamond_t = SignedFormula("T", Possibility(A))
    signed_formula_diamond_f = SignedFormula("F", Possibility(A))

    new_signed_formulas_box_t = tableau_prover._handle_modal_operators(signed_formula_box_t)
    new_signed_formulas_box_f = tableau_prover._handle_modal_operators(signed_formula_box_f)
    new_signed_formulas_diamond_t = tableau_prover._handle_modal_operators(signed_formula_diamond_t)
    new_signed_formulas_diamond_f = tableau_prover._handle_modal_operators(signed_formula_diamond_f)

    # Assertions for Necessity(T)
    assert len(new_signed_formulas_box_t) == 1
    assert new_signed_formulas_box_t[0].sign == "T"
    assert new_signed_formulas_box_t[0].formula == A

    # Assertions for Necessity(F)
    assert len(new_signed_formulas_box_f) == 1
    assert new_signed_formulas_box_f[0].sign == "F"
    assert new_signed_formulas_box_f[0].formula == A

    # Assertions for Possibility(T)
    assert len(new_signed_formulas_diamond_t) == 1
    assert new_signed_formulas_diamond_t[0].sign == "T"
    assert new_signed_formulas_diamond_t[0].formula == A

    # Assertions for Possibility(F)
    assert len(new_signed_formulas_diamond_f) == 1
    assert new_signed_formulas_diamond_f[0].sign == "F"
    assert new_signed_formulas_diamond_f[0].formula == A


def test_handle_not(tableau_prover):
    A = Proposition("A")
    signed_formula = SignedFormula("T", Not(A))
    new_signed_formulas = tableau_prover._handle_not(signed_formula)
    # Add your assertions here, e.g.,
    assert len(new_signed_formulas) == 1
