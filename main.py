from symlogos.functions_and_predicates import Proposition, Predicate, Forall, Exists, HigherOrderFunction, Implication

def demonstrate_propositions():
    print("=== Propositions ===")
    p = Proposition("p")
    not_p = p.neg()
    box_p = p.box()
    diamond_p = p.diamond()

    print("p:", p)
    print("¬p:", not_p)
    print("□p:", box_p)
    print("◇p:", diamond_p)
    print()

def demonstrate_predicates_quantifiers():
    print("=== Predicates and Quantifiers ===")
    Px = Predicate("P", "x")
    Py = Predicate("P", "y")
    forall_px = Forall("x", Px)
    exists_py = Exists("y", Py)

    print("Px:", Px)
    print("Py:", Py)
    print("∀xPx:", forall_px)
    print("∃yPy:", exists_py)
    print()

def demonstrate_higher_order_functions():
    print("=== Higher-Order Functions ===")
    F = HigherOrderFunction("F")
    p = Proposition("p")
    f_of_p = F(p)
    box_f_of_p = F(p).box()

    print("F(p):", f_of_p)
    print("□F(p):", box_f_of_p)
    print()

def demonstrate_implications():
    print("=== Implications ===")
    p = Proposition("p")
    q = Proposition("q")
    p_implies_q = Implication(p, q)
    not_p_implies_not_q = Implication(p.neg(), q.neg())

    print("p -> q:", p_implies_q)
    print("¬p -> ¬q:", not_p_implies_not_q)
    print()

if __name__ == "__main__":
    demonstrate_propositions()
    demonstrate_predicates_quantifiers()
    demonstrate_higher_order_functions()
    demonstrate_implications()
