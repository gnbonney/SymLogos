from sympy import symbols
from symlogos import Proposition, And, Not, Necessity, Possibility, Predicate, Forall, Exists

def test_negation():
    p = Proposition('p')
    not_p = Not(p)
    assert str(not_p) == '¬p'

def test_box_operator():
    p = Proposition('p')
    box_p = Necessity(p)
    assert str(box_p) == '□p'

def test_diamond_operator():
    p = Proposition('p')
    diamond_p = Possibility(p)
    assert str(diamond_p) == '◇p'

def test_expression_string_representation():
    p = Proposition('p')
    not_p = Not(p)
    assert str(not_p) == '¬p'

def test_expression_complex_operations():
    p, q = Proposition("p"), Proposition("q")
    expr = Not(And(p, q))
    assert str(expr) == "¬(p ∧ q)"

def test_expression_complex_operations_2():
    p, q = Proposition("p"), Proposition("q")
    expr = Necessity(And(p, q))
    assert str(expr) == "□(p ∧ q)"

def test_expression_complex_operations_3():
    p, q = Proposition("p"), Proposition("q")
    expr = Possibility(And(p, q))
    assert str(expr) == "◇(p ∧ q)"

def test_predicate():
    x, y = symbols("x y")
    Px = Predicate("P", x)
    assert str(Px) == "P(x)"
    Py = Predicate("P", y)
    assert str(Py) == "P(y)"

def test_forall():
    x = symbols("x")
    Px = Predicate("P", x)
    forall_px = Forall(x, Px)
    assert str(forall_px) == "∀x: P(x)"

def test_exists():
    y = symbols("y")
    Py = Predicate("P", y)
    exists_py = Exists(y, Py)
    assert str(exists_py) == "∃y: P(y)"