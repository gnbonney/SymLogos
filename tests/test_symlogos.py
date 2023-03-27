from symlogos import Proposition, And, Not, Necessity, Possibility

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

