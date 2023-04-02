import abc
import sympy

class CombinedMeta(sympy.Basic.__class__, abc.ABCMeta):
    pass

class LogicalExpression(sympy.Basic, metaclass=CombinedMeta):
    @abc.abstractmethod
    def __eq__(self, other):
        pass

    @abc.abstractmethod
    def __hash__(self):
        pass

    @abc.abstractmethod
    def match(self, other):
        pass

    def substitute(self, mapping):
        raise NotImplementedError("Substitution not implemented for this class")

    def substitute_all(self, substitutions):
        return self.subs(substitutions)

    def substitute_all_terms(self, term_replacement_dict):
        return self.subs(term_replacement_dict)

    def evaluate(self, assignment):
        return self.subs(assignment).evalf()

    def is_atomic(self):
        return False

    def to_nnf(self):
        if self.is_atomic():
            return self
        else:
            raise NotImplementedError(f"to_nnf is not implemented for the class {type(self)}")




class Term(sympy.Basic):
    def __new__(cls, name):
        obj = super().__new__(cls)
        obj.symbol = sympy.Symbol(name)
        return obj

    def __eq__(self, other):
        if isinstance(other, Term):
            return self.symbol == other.symbol
        return False

    def __hash__(self):
        return hash((type(self), self.symbol))

    def __str__(self):
        return str(self.symbol)

    def __repr__(self):
        return f"Term('{self.symbol}')"

    def substitute(self, mapping):
        if self in mapping:
            return mapping[self]
        return self

    def evaluate(self, assignment):
        if self.symbol in assignment:
            return assignment[self.symbol]
        else:
            raise ValueError(f"Assignment for term '{self.symbol}' not found.")

    def match(self, other):
        if isinstance(other, Term):
            if self.symbol == other.symbol:
                print(f"Match successful: self: {self}, other: {other}")
                return {}
            elif self.is_variable() or other.is_variable():
                print(f"Match successful: self: {self}, other: {other}")
                return {self: other}
            else:
                print(f"Matching failed for terms: self: {self}, other: {other}")
                return None
        else:
            print(f"Matching failed for different types: self: {self}, other: {other}")
            return None

    def is_variable(self):
        return self.symbol.name.islower()
    
def simplify_expression(expr):
    if isinstance(expr, LogicalExpression):
        return expr.simplify()
    return expr
