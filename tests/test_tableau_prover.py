import pytest
from symlogos.expressions_and_terms import Term
from symlogos.connectives import And, Or, Implication
from symlogos.functions_and_predicates import Predicate
from symlogos.modal_operators import Necessity
from symlogos.quantifiers import Forall, Exists
from symlogos.signed_formula import SignedFormula
from symlogos.tableau_prover import TableauProver, TableauNode
from symlogos.first_order_rules import AlphaRule, BetaRule, GammaRule, DeltaRule
from symlogos.proposition import Proposition


def test_alpha_rule():
    f1 = And(Term("A"), Term("B"))
    sf = SignedFormula("T", f1)

    alpha_rule = AlphaRule(sf)
    assert alpha_rule.is_applicable()
    new_signed_formulas = alpha_rule.apply()
    assert len(new_signed_formulas) == 2
    assert SignedFormula("T", Term("A")) in new_signed_formulas
    assert SignedFormula("T", Term("B")) in new_signed_formulas

def test_beta_rule():
    f1 = Implication(Term("A"), Term("B"))
    sf = SignedFormula("T", f1)

    beta_rule = BetaRule(sf)
    assert beta_rule.is_applicable()
    new_signed_formulas = beta_rule.apply()
    assert len(new_signed_formulas) == 2
    assert SignedFormula("F", Term("A")) in new_signed_formulas
    assert SignedFormula("T", Term("B")) in new_signed_formulas

def test_gamma_rule():
    x = Term("x")
    P = Predicate("P", x)
    f1 = Exists(x, P)
    sf = SignedFormula("F", f1)

    gamma_rule = GammaRule(sf)

    node = TableauNode(sf)
    gamma_rule.apply(node)

    # Check if the node has exactly one child
    assert len(node.children) == 1

    # Check if the child node has the correct signed formula
    child_signed_formula = node.children[0].signed_formula
    fresh_variable = Term("v_0")
    expected_signed_formula = SignedFormula("T", P.substitute({x: fresh_variable}))
    assert child_signed_formula == expected_signed_formula

def test_delta_rule():
    x = Term("x")
    P = Predicate("P", [x])
    f1 = Forall(x, P)
    sf = SignedFormula("F", f1)

    delta_rule = DeltaRule(sf)

    node = TableauNode(sf)
    delta_rule.apply(node)

    assert len(node.children) == 1
    assert node.children[0].signed_formula == SignedFormula("T", Predicate("P", [Term("v_0")]))

def is_tableau_structure_correct(tableau, expected_structure):
    def _compare_nodes(node, expected_node):
        if not node or not expected_node:
            return False
        
        if node.signed_formula != expected_node.signed_formula:
            return False
        
        if len(node.children) != len(expected_node.children):
            return False
        
        for child, expected_child in zip(node.children, expected_node.children):
            if not _compare_nodes(child, expected_child):
                return False
        
        return True

    return _compare_nodes(tableau, expected_structure)

def test_tableau_structure_correct_and():
    A = Proposition("A")
    B = Proposition("B")

    conjunction = And(A, B)
    tableau_root = TableauNode(SignedFormula("T", conjunction))

    tableau_A = TableauNode(SignedFormula("T", A))
    tableau_B = TableauNode(SignedFormula("T", B))

    tableau_root.children = [tableau_A, tableau_B]

    expected_structure = tableau_root

    assert is_tableau_structure_correct(tableau_root, expected_structure)


def test_tableau_structure_correct_or():
    A = Proposition("A")
    B = Proposition("B")

    disjunction = Or(A, B)
    tableau_root = TableauNode(SignedFormula("T", disjunction))

    tableau_A = TableauNode(SignedFormula("T", A))
    tableau_B = TableauNode(SignedFormula("T", B))

    tableau_root.children = [tableau_A]
    tableau_A.children = [tableau_B]

    expected_structure = tableau_root

    assert is_tableau_structure_correct(tableau_root, expected_structure)


def test_tableau_structure_correct_implication():
    A = Proposition("A")
    B = Proposition("B")

    implication = Implication(A, B)
    tableau_root = TableauNode(SignedFormula("T", implication))

    tableau_A = TableauNode(SignedFormula("F", A))
    tableau_B = TableauNode(SignedFormula("T", B))

    tableau_root.children = [tableau_A, tableau_B]

    expected_structure = tableau_root

    assert is_tableau_structure_correct(tableau_root, expected_structure)

def test_tableau_prover():
    A = Proposition("A")
    B = Proposition("B")
    C = Proposition("C")

    # Example: A -> (B -> A)
    premises = []
    conclusion = Implication(A, Implication(B, A))
    prover = TableauProver()
    assert prover.is_sound(premises, conclusion)

    # Example: (A -> B), A |- B
    premises = [Implication(A, B), A]
    conclusion = B
    prover = TableauProver()
    assert prover.is_sound(premises, conclusion)

    # Example: (A -> B), (B -> C), A |- C
    premises = [Implication(A, B), Implication(B, C), A]
    conclusion = C
    prover = TableauProver()
    assert prover.is_sound(premises, conclusion)

    # Example: A -> (B -> A)
    premises = []
    conclusion = Implication(A, Implication(B, A))
    prover = TableauProver()
    assert prover.is_sound(premises, conclusion)

    # Example: A, (A -> B), (B -> C) |- C
    premises = [A, Implication(A, B), Implication(B, C)]
    conclusion = C
    prover = TableauProver()
    assert prover.is_sound(premises, conclusion)

    # Example: (A and B) -> (B and A)
    premises = []
    conclusion = Implication(And(A, B), And(B, A))
    prover = TableauProver()
    assert prover.is_sound(premises, conclusion)

    # Example: (A or B) -> (B or A)
    premises = []
    conclusion = Implication(Or(A, B), Or(B, A))
    prover = TableauProver()
    assert prover.is_sound(premises, conclusion)

def test_modal_tableau_prover():
    A = Proposition("A")

    # Example: (□A -> A) -> A
    premises = []
    conclusion = Implication(Implication(Necessity(A), A), A)
    prover = TableauProver()
    assert prover.is_sound(premises, conclusion)