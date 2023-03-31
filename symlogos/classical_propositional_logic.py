from .connectives import Implication, And, Or, Not
from .proposition import Proposition
from .rules import Rule

class ClassicalPropositionalLogic:

    @staticmethod
    def modus_ponens():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Modus Ponens", [p, Implication(p, q)], q)

    @staticmethod
    def modus_tollens():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Modus Tollens", [Implication(p, q), Not(q)], Not(p))

    @staticmethod
    def disjunction_introduction():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Disjunction Introduction", [p], Or(p, q))

    @staticmethod
    def disjunction_elimination():
        p = Proposition("p")
        q = Proposition("q")
        r = Proposition("r")
        return Rule("Disjunction Elimination", [Or(p, q), Implication(p, r), Implication(q, r)], r)

    @staticmethod
    def conjunction_introduction():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Conjunction Introduction", [p, q], And(p, q))

    @staticmethod
    def conjunction_elimination1():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Conjunction Elimination 1", [And(p, q)], p)

    @staticmethod
    def conjunction_elimination2():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Conjunction Elimination 2", [And(p, q)], q)


    @staticmethod
    def commutativity_and():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Commutativity of And", [And(p, q)], And(q, p))

    @staticmethod
    def commutativity_or():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Commutativity of Or", [Or(p, q)], Or(q, p))

    @staticmethod
    def associativity_and():
        p = Proposition("p")
        q = Proposition("q")
        r = Proposition("r")
        return Rule("Associativity of And", [And(p, And(q, r))], And(And(p, q), r))

    @staticmethod
    def associativity_or():
        p = Proposition("p")
        q = Proposition("q")
        r = Proposition("r")
        return Rule("Associativity of Or", [Or(p, Or(q, r))], Or(Or(p, q), r))

    @staticmethod
    def idempotency_and():
        p = Proposition("p")
        return Rule("Idempotency of And", [And(p, p)], p)

    @staticmethod
    def idempotency_or():
        p = Proposition("p")
        return Rule("Idempotency of Or", [Or(p, p)], p)

    @staticmethod
    def double_negation_elimination():
        p = Proposition("p")
        return Rule("Double Negation Elimination", [Not(Not(p))], p)

    @staticmethod
    def distribution_and_over_or():
        p = Proposition("p")
        q = Proposition("q")
        r = Proposition("r")
        return Rule("Distribution of And over Or", [And(p, Or(q, r))], Or(And(p, q), And(p, r)))

    @staticmethod
    def distribution_or_over_and():
        p = Proposition("p")
        q = Proposition("q")
        r = Proposition("r")
        return Rule("Distribution of Or over And", [Or(p, And(q, r))], And(Or(p, q), Or(p, r)))

    @staticmethod
    def absorption_and():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Absorption of And", [And(p, Or(p, q))], p)

    @staticmethod
    def absorption_or():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Absorption of Or", [Or(p, And(p, q))], p)

    @staticmethod
    def negation_and_to_or():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Negation of And to Or", [Not(And(p, q))], Or(Not(p), Not(q)))

    @staticmethod
    def negation_or_to_and():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Negation of Or to And", [Not(Or(p, q))], And(Not(p), Not(q)))

    @staticmethod
    def implication_to_or():
        p = Proposition("p")
        q = Proposition("q")
        return Rule("Implication to Or", [Implication(p, q)], Or(Not(p), q))
