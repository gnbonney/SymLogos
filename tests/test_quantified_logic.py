from symlogos.proposition import Proposition
from symlogos.quantified_logic import QuantifiedLogic
from symlogos.quantifiers import Exists
from symlogos.modal_operators import Necessity
from symlogos.quantifiers import Forall

def test_existential_instantiation():
    x = Proposition("x")
    Fx = Proposition("Fx")
    c = Proposition("c")
    rule = QuantifiedLogic.existential_instantiation()
    premises = [Exists(x, Fx)]
    expected_result = Fx.substitute(x, c)
    result = rule.apply(*premises)
    assert result == expected_result


def test_barcan_formula():
    x = Proposition("x")
    Fx = Proposition("Fx")
    rule = QuantifiedLogic.barcan_formula()
    premises = [Necessity(Forall(x, Fx))]
    expected_result = Forall(x, Necessity(Fx))
    result = rule.apply(*premises)
    assert result == expected_result