from .proposition import Proposition
from .rules import Rule
from .modal_logic import Necessity
from .quantifiers import Exists, Forall
from symlogos.rules import Rule

class QuantifiedLogic:
    @staticmethod
    def existential_instantiation() -> Rule:
        x = Proposition("x")
        Fx = Proposition("Fx")
        c = Proposition("c")
        return Rule("Existential Instantiation", [Exists(x, Fx)], Fx.substitute(x, c))

    @staticmethod
    def barcan_formula() -> Rule:
        x = Proposition("x")
        Fx = Proposition("Fx")
        return Rule("Barcan Formula", [Necessity(Forall(x, Fx))], Forall(x, Necessity(Fx)))
