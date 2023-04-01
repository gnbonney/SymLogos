from symlogos.expressions_and_terms import Term
from symlogos.quantifiers import Forall
from symlogos.functions_and_predicates import Predicate, HigherOrderFunction, FunctionApplication

# def test_function_application_predicate():
#     x = Term("x")
#     y = Term("y")
#     R = Predicate("R", 2)
#     relation_application = FunctionApplication(R, x, y)
#     assert relation_application == FunctionApplication(Predicate("R", 2), Term("x"), Term("y"))

def test_function_application_higher_order():
    x = Term("x")
    g = Predicate("g", 1)
    h = HigherOrderFunction("h", return_function=g)
    higher_order_application = FunctionApplication(h, x)
    assert higher_order_application == FunctionApplication(HigherOrderFunction("h", return_function=Predicate("g", 1)), Term("x"))

def test_forall_application():
    x = Term("x")
    P = Predicate("P", x)
    forall_px = Forall(x, P)
    assert forall_px == Forall(Term("x"), Predicate("P", Term("x")))
