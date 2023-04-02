import pytest
from symlogos.expressions_and_terms import LogicalExpression
from symlogos.proposition import Proposition
from symlogos.quantifiers import Forall, Exists
from symlogos.functions_and_predicates import Predicate
from symlogos.connectives import Implication, Not, And, Or
from symlogos.rules import Rule

def test_proposition_to_nnf():
    p = Proposition("p")
    assert p.to_nnf() == p

def test_not_to_nnf():
    p = Proposition("p")
    not_p = Not(p)
    assert not_p.to_nnf() == not_p

def test_and_to_nnf():
    p = Proposition("p")
    q = Proposition("q")
    and_expr = And(p, q)
    assert and_expr.to_nnf() == and_expr

def test_or_to_nnf():
    p = Proposition("p")
    q = Proposition("q")
    or_expr = Or(p, q)
    assert or_expr.to_nnf() == or_expr

def test_forall_to_nnf():
    Px = Predicate("P", "x")
    forall_px = Forall("x", Px)
    assert forall_px.to_nnf() == forall_px

def test_exists_to_nnf():
    Px = Predicate("P", "x")
    exists_px = Exists("x", Px)
    assert exists_px.to_nnf() == exists_px

def test_logical_expression_to_nnf_not_implemented():
    class DummyExpression(LogicalExpression):
        def __eq__(self, other):
            return isinstance(other, DummyExpression)

        def __hash__(self):
            return hash(type(self))

        def match(self, pattern):
            return isinstance(pattern, DummyExpression)

    dummy_expr = DummyExpression()
    with pytest.raises(NotImplementedError):
        dummy_expr.to_nnf()

def test_rule_to_nnf():
    # Define propositions
    p = Proposition("p")
    q = Proposition("q")

    # Define logical expressions
    not_p = Not(p)
    not_q = Not(q)
    p_implies_q = Implication(p, q)

    # Create a rule with premises and a conclusion
    rule = Rule("Implication elimination", [p_implies_q, p], q)

    # Call the to_nnf method on the rule object
    nnf_rule = rule.to_nnf()

    # Check if the premises and conclusion of the nnf_rule are in NNF
    assert nnf_rule.premises[0] == p_implies_q.to_nnf()
    assert nnf_rule.premises[1] == p.to_nnf()
    assert nnf_rule.conclusion == q.to_nnf()

