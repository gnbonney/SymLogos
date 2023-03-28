from sympy import symbols
from symlogos import Proposition, And, Not, Necessity, Possibility, Predicate, Forall, Exists, HigherOrderFunction

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

def test_higher_order_function():
    f = HigherOrderFunction("f")
    assert str(f) == "f"
    assert repr(f) == "HigherOrderFunction('f', None, None)"

def test_higher_order_function_with_arg_function():
    g = HigherOrderFunction("g")
    f_of_g = HigherOrderFunction("f", arg_function=g)
    assert str(f_of_g) == "f(g)"
    assert repr(f_of_g) == "HigherOrderFunction('f', HigherOrderFunction('g', None, None), None)"

def test_higher_order_function_with_return_function():
    g = HigherOrderFunction("g")
    f_to_g = HigherOrderFunction("f", return_function=g)
    assert str(f_to_g) == "f -> g"
    assert repr(f_to_g) == "HigherOrderFunction('f', None, HigherOrderFunction('g', None, None))"

def test_higher_order_function_with_arg_and_return_function():
    h = HigherOrderFunction("h")
    g = HigherOrderFunction("g")
    f_of_h_to_g = HigherOrderFunction("f", arg_function=h, return_function=g)
    assert str(f_of_h_to_g) == "f(h) -> g"
    assert repr(f_of_h_to_g) == "HigherOrderFunction('f', HigherOrderFunction('h', None, None), HigherOrderFunction('g', None, None))"
