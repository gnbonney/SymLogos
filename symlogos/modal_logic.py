from .proposition import Proposition
from symlogos.connectives import Implication
from .modal_operators import Necessity, Possibility
from .rules import Rule

class ModalLogic:
    @staticmethod
    def necessitation():
        p = Proposition("p")
        return Rule("Necessitation", [p], Necessity(p))

    @staticmethod
    def distribution_axiom():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Distribution Axiom", [Necessity(Implication(p, q))], Implication(Necessity(p), Necessity(q)))

    @staticmethod
    def possibility_axiom():
        p = Proposition("p")
        return Rule("Possibility Axiom", [Possibility(p)], Necessity(Possibility(p)))

    @staticmethod
    def modal_modus_ponens():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Modal Modus Ponens", [Necessity(Implication(p, q)), Necessity(p)], Necessity(q))

    @staticmethod
    def t_schema():
        p = Proposition("p")
        return Rule("T-schema", [Necessity(p)], p)
