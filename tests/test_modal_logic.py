from symlogos.modal_logic import ModalLogic
from symlogos.proposition import Proposition
from symlogos.modal_operators import Necessity, Possibility
from symlogos.connectives import Implication

def test_necessitation():
    p = Proposition("p")
    rule = ModalLogic.necessitation()
    premises = [p]
    expected_result = Necessity(p)
    result = rule.apply(*premises)
    assert result == expected_result


def test_distribution_axiom():
    p = Proposition("p")
    q = Proposition("q")
    rule = ModalLogic.distribution_axiom()
    premises = [Necessity(Implication(p, q))]
    expected_result = Implication(Necessity(p), Necessity(q))
    result = rule.apply(*premises)
    assert result == expected_result


def test_possibility_axiom():
    p = Proposition("p")
    rule = ModalLogic.possibility_axiom()
    premises = [Possibility(p)]
    expected_result = Necessity(Possibility(p))
    result = rule.apply(*premises)
    assert result == expected_result


def test_modal_modus_ponens():
    p = Proposition("p")
    q = Proposition("q")
    rule = ModalLogic.modal_modus_ponens()
    premises = [Necessity(Implication(p, q)), Necessity(p)]
    expected_result = Necessity(q)
    result = rule.apply(*premises)
    assert result == expected_result


def test_t_schema():
    p = Proposition("p")
    rule = ModalLogic.t_schema()
    premises = [Necessity(p)]
    expected_result = p
    result = rule.apply(*premises)
    assert result == expected_result
