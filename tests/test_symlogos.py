from sympy import symbols, Symbol
from symlogos.axiom_set import AxiomSet
from symlogos.connectives import Implication, And, Not
from symlogos.expressions_and_terms import LogicalExpression, Term
from symlogos.functions_and_predicates import Predicate, HigherOrderFunction, FunctionApplication
from symlogos.modal_operators import Possibility, Necessity
from symlogos.proposition import Proposition
from symlogos.quantifiers import Forall, Exists
from symlogos.rules import Rule

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

def test_forall_substitution():
    x = Term("x")
    c = Term("c")
    P = Predicate("P", x)
    forall_px = Forall(x, P)
    result = forall_px.substitute({x: c})
    assert result == Forall(c, Predicate("P", c))

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
    q = Proposition("q")
    assignment = {p: True, q: False}
    assert p.evaluate(assignment) == True
    assert q.evaluate(assignment) == False


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

def test_term_creation():
    t = Term('x')
    assert isinstance(t, Term)
    assert t.symbol == Symbol('x')

def test_term_str():
    t = Term('x')
    assert str(t) == 'x'

def test_term_repr():
    t = Term('x')
    assert repr(t) == "Term('x')"

def test_rule_creation():
    A = Term('A')
    B = Term('B')
    f = FunctionApplication('f', A)
    g = FunctionApplication('g', B)
    
    rule = Rule('example_rule', [f], g)
    
    assert isinstance(rule, Rule)
    assert rule.name == 'example_rule'
    assert rule.premises == [f]
    assert rule.conclusion == g
    assert str(rule) == "example_rule: f(A) ⊢ g(B)"

def test_rule_str():
    premise1 = Term('x')
    premise2 = Term('y')
    conclusion = Term('z')
    rule = Rule('R1', [premise1, premise2], conclusion)

    assert str(rule) == "R1: x, y ⊢ z"

def test_rule_repr():
    premise1 = Term('x')
    premise2 = Term('y')
    conclusion = Term('z')
    rule = Rule('R1', [premise1, premise2], conclusion)

    assert repr(rule) == "Rule('R1', [Term('x'), Term('y')], Term('z'))"

def test_rule_apply():
    x = Term("x")
    y = Term("y")
    P = Predicate("P", x)
    Q = Predicate("Q", y)
    R = Predicate("R", x, y)
    premise1 = P
    premise2 = Q
    conclusion = R
    rule = Rule("TestRule", [premise1, premise2], conclusion)

    a = Term("a")
    b = Term("b")
    result = rule.apply(Predicate("P", a), Predicate("Q", b))
    assert result == Predicate("R", a, b)

def test_modus_ponens():
    p = Proposition("p")
    q = Proposition("q")
    modus_ponens = Rule("Modus Ponens", [Implication(p, q), p], q)

    premise1 = Implication(p, q)
    premise2 = p

    result = modus_ponens.apply(premise1, premise2)
    assert result == q


def test_modus_tollens():
    p = Proposition("p")
    q = Proposition("q")
    modus_tollens = Rule("Modus Tollens", [Implication(p, q), Not(q)], Not(p))

    premise1 = Implication(p, q)
    premise2 = Not(q)

    result = modus_tollens.apply(premise1, premise2)
    assert result == Not(p)

def test_universal_instantiation():
    x = Term("x")
    c = Term("c")
    P = Predicate("P", x)
    forall_px = Forall(x, P)
    universal_instantiation = Rule("Universal Instantiation", [forall_px], Predicate("P", c))

    premise = forall_px
    result = universal_instantiation.apply(premise)
    assert result == Predicate("P", c)

def test_existential_instantiation():
    x = Term("x")
    P = Predicate("P", x)
    premise = Exists(x, P)
    rule = Rule("Existential Instantiation", [premise], P)

    a = Term("a")
    result = rule.apply(Exists(x, Predicate("P", a)))

    assert result == Predicate("P", a)

def test_modal_modus_ponens():
    p = Proposition("p")
    q = Proposition("q")
    box_p_implies_q = Necessity(Implication(p, q))
    box_p = Necessity(p)

    modal_modus_ponens = Rule("Modal Modus Ponens", [box_p_implies_q, box_p], Necessity(q))
    premise1 = box_p_implies_q
    premise2 = box_p

    result = modal_modus_ponens.apply(premise1, premise2)
    assert result == Necessity(q)

def test_barcan_formula():
    x = Term("x")
    P = Predicate("P", x)
    forall_P = Forall(x, P)
    box_forall_P = Necessity(forall_P)
    box_P = Necessity(P)
    forall_box_P = Forall(x, box_P)
    
    barcan_formula = Rule("Barcan Formula", [forall_box_P], box_forall_P)
    premise = forall_box_P
    
    result = barcan_formula.apply(premise)
    
    assert result == box_forall_P