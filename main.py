from symlogos.functions_and_predicates import Proposition, Term, FunctionApplication, Predicate, Forall, Exists, Implication

def demonstrate_propositions():
    print("=== Propositions ===")
    p = Proposition("p")
    not_p = ~p
    box_p = p.box()
    diamond_p = p.diamond()

    print("p:", p)
    print("¬p:", not_p)
    print("□p:", box_p)
    print("◇p:", diamond_p)
    print()

def demonstrate_predicates_quantifiers():
    print("=== Predicates and Quantifiers ===")
    x = Term("x")
    y = Term("y")
    Px = Predicate("P", x)
    Py = Predicate("P", y)
    forall_px = Forall(x, Px)
    exists_py = Exists(y, Py)

    print("Px:", Px)
    print("Py:", Py)
    print("∀xPx:", forall_px)
    print("∃yPy:", exists_py)
    print()

def demonstrate_function_application():
    print("=== Function Application ===")
    x = Term("x")
    y = Term("y")
    f = FunctionApplication("f", x)
    g = FunctionApplication("g", y)

    print("f(x):", f)
    print("g(y):", g)
    print()

def demonstrate_implications():
    print("=== Implications ===")
    p = Proposition("p")
    q = Proposition("q")
    p_implies_q = Implication(p, q)
    not_p_implies_not_q = Implication(~p, ~q)

    print("p -> q:", p_implies_q)
    print("¬p -> ¬q:", not_p_implies_not_q)
    print()

if __name__ == "__main__":
    demonstrate_propositions()
    demonstrate_predicates_quantifiers()
    demonstrate_function_application()
    demonstrate_implications()
