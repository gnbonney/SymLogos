from symlogos.classical_propositional_logic import *
from symlogos.connectives import Implication, And, Or, Not
from symlogos.proposition import Proposition


def test_modus_ponens():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.modus_ponens()
    premises = [p, Implication(p, q)]
    expected_result = q

    result = rule.apply(*premises)
    assert result == expected_result

def test_modus_tollens():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.modus_tollens()
    premises = [Implication(p, q), Not(q)]
    expected_result = Not(p)

    result = rule.apply(*premises)
    assert result == expected_result

def test_disjunction_introduction():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.disjunction_introduction()
    premises = [p]
    expected_result = Or(p, q)

    result = rule.apply(*premises)
    assert result == expected_result

def test_disjunction_elimination():
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")
    rule = ClassicalPropositionalLogic.disjunction_elimination()
    premises = [Or(p, q), Implication(p, r), Implication(q, r)]
    expected_result = r

    result = rule.apply(*premises)
    assert result == expected_result

def test_conjunction_introduction():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.conjunction_introduction()
    premises = [p, q]
    expected_result = And(p, q)

    result = rule.apply(*premises)
    assert result == expected_result

def test_conjunction_elimination1():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.conjunction_elimination1()
    premises = [And(p, q)]
    expected_result = p

    result = rule.apply(*premises)
    assert result == expected_result

def test_conjunction_elimination2():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.conjunction_elimination2()
    premises = [And(p, q)]
    expected_result = q

    result = rule.apply(*premises)
    assert result == expected_result

def test_distribution_and_over_or():
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")
    rule = ClassicalPropositionalLogic.distribution_and_over_or()
    premise = And(p, Or(q, r))
    expected_result = Or(And(p, q), And(p, r))

    result = rule.apply(premise)
    assert result == expected_result

def test_distribution_or_over_and():
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")
    rule = ClassicalPropositionalLogic.distribution_or_over_and()
    premise = Or(p, And(q, r))
    expected_result = And(Or(p, q), Or(p, r))

    result = rule.apply(premise)
    assert result == expected_result

def test_absorption_and():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.absorption_and()
    premise = And(p, Or(p, q))
    expected_result = p

    result = rule.apply(premise)
    assert result == expected_result

def test_absorption_or():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.absorption_or()
    premise = Or(p, And(p, q))
    expected_result = p

    result = rule.apply(premise)
    assert result == expected_result

def test_negation_and_to_or():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.negation_and_to_or()
    premise = Not(And(p, q))
    expected_result = Or(Not(p), Not(q))

    result = rule.apply(premise)
    assert result == expected_result

def test_negation_or_to_and():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.negation_or_to_and()
    premise = Not(Or(p, q))
    expected_result = And(Not(p), Not(q))

    result = rule.apply(premise)
    assert result == expected_result

def test_implication_to_or():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.implication_to_or()
    premise = Implication(p, q)
    expected_result = Or(Not(p), q)

    result = rule.apply(premise)
    assert result == expected_result

def test_commutativity_and():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.commutativity_and()
    premises = [And(p, q)]
    expected_result = And(q, p)

    result = rule.apply(*premises)
    assert result == expected_result

def test_commutativity_or():
    p = Proposition("p")
    q = Proposition("q")
    rule = ClassicalPropositionalLogic.commutativity_or()
    premises = [Or(p, q)]
    expected_result = Or(q, p)

    result = rule.apply(*premises)
    assert result == expected_result

def test_associativity_and():
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")
    rule = ClassicalPropositionalLogic.associativity_and()
    premises = [And(p, And(q, r))]
    expected_result = And(And(p, q), r)

    result = rule.apply(*premises)
    assert result == expected_result

def test_associativity_or():
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")
    rule = ClassicalPropositionalLogic.associativity_or()
    premises = [Or(p, Or(q, r))]
    expected_result = Or(Or(p, q), r)

    result = rule.apply(*premises)
    assert result == expected_result

def test_idempotency_and():
    p = Proposition("p")
    rule = ClassicalPropositionalLogic.idempotency_and()
    premises = [And(p, p)]
    expected_result = p

    result = rule.apply(*premises)
    assert result == expected_result

def test_idempotency_or():
    p = Proposition("p")
    rule = ClassicalPropositionalLogic.idempotency_or()
    premises = [Or(p, p)]
    expected_result = p

    result = rule.apply(*premises)
    assert result == expected_result

def test_double_negation_elimination():
    p = Proposition("p")
    rule = ClassicalPropositionalLogic.double_negation_elimination()
    premises = [Not(Not(p))]
    expected_result = p

    result = rule.apply(*premises)
    assert result == expected_result
