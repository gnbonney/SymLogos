from .proposition import Proposition
from .rules import Rule
from .modal_logic import Necessity
from .quantifiers import Exists, Forall

class QuantifiedLogic:
    @staticmethod
    def existential_instantiation():
        x = Proposition("x")
        Fx = Proposition("Fx")
        c = Proposition("c")
        return Rule("Existential Instantiation", [Exists(x, Fx)], Fx.substitute(x, c))

    @staticmethod
    def barcan_formula():
        x = Proposition("x")
        Fx = Proposition("Fx")
        return Rule("Barcan Formula", [Necessity(Forall(x, Fx))], Forall(x, Necessity(Fx)))
