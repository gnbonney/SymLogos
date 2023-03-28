from sympy import symbols
from symlogos import *

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

def test_substitute():
    p, q = Proposition("p"), Proposition("q")
    not_p = Not(p)
    not_q = Not(q)
    assert not_p.substitute(p, q) == not_q

    and_pq = And(p, q)
    and_pr = And(p, p)
    assert and_pq.substitute(q, p) == and_pr


def test_evaluate():
    p = Proposition("p")
    assignment = {"p": True}
    assert p.evaluate(assignment) == True


def test_simplify():
    p, q = Proposition("p"), Proposition("q")
    and_true_p = And(True, p)
    assert and_true_p.simplify() == p

    and_false_p = And(False, p)
    assert and_false_p.simplify() == False

    not_true = Not(True)
    assert not_true.simplify() == False

    not_false = Not(False)
    assert not_false.simplify() == True

    not_not_p = Not(Not(p))
    assert not_not_p.simplify() == p

    necessity_true = Necessity(True)
    assert necessity_true.simplify() == True

    possibility_true = Possibility(True)
    assert possibility_true.simplify() == True


def test_complex_simplify():
    p, q = Proposition("p"), Proposition("q")
    complex_expr = And(p, Not(Not(q)))
    simplified_expr = And(p, q)
    assert complex_expr.simplify() == simplified_expr

def test_add_remove_axiom():
    axiom_set = AxiomSet()
    p = Proposition("p")
    q = Proposition("q")

    assert len(axiom_set) == 0
    assert p not in axiom_set

    axiom_set.add_axiom(p)
    assert len(axiom_set) == 1
    assert p in axiom_set

    axiom_set.add_axiom(q)
    assert len(axiom_set) == 2
    assert q in axiom_set

    axiom_set.remove_axiom(p)
    assert len(axiom_set) == 1
    assert p not in axiom_set
    assert q in axiom_set

def test_iterate_axioms():
    axiom_set = AxiomSet()
    p = Proposition("p")
    q = Proposition("q")

    axiom_set.add_axiom(p)
    axiom_set.add_axiom(q)

    axiom_list = [axiom for axiom in axiom_set]

    assert p in axiom_list
    assert q in axiom_list

def test_repr():
    axiom_set = AxiomSet()
    p = Proposition("p")
    q = Proposition("q")

    axiom_set.add_axiom(p)
    axiom_set.add_axiom(q)

    assert "p" in repr(axiom_set)
    assert "q" in repr(axiom_set)