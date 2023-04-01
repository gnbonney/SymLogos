import sympy
from .expressions_and_terms import LogicalExpression

class Proposition(LogicalExpression):
    def __new__(cls, name):
        obj = super().__new__(cls)
        obj.name = sympy.Symbol(name)
        return obj

    def __eq__(self, other):
        if isinstance(other, Proposition):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash((type(self), self.name))

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"Proposition('{self.name}')"

    def match(self, other, bindings=None):
        if bindings is None:
            bindings = {}

        if isinstance(other, Proposition):
            if self.name == other.name:
                return bindings
            elif self.is_variable() or other.is_variable():
                if self not in bindings:
                    bindings[self] = other
                    return bindings
                elif bindings[self] == other:
                    return bindings
            return None
        return None

    def evaluate(self, assignment):
        return assignment.get(self, self)

    def simplify(self):
        return self

    def substitute(self, variable, replacement):
        if self == variable:
            return replacement
        else:
            return self

    def substitute_all(self, substitutions):
        new_attributes = {}
        for attr, value in self.__dict__.items():
            if isinstance(value, sympy.Basic):
                new_attributes[attr] = value.subs(substitutions)
            else:
                new_attributes[attr] = value
        result = self.__class__(*new_attributes.values())
        return result

    def substitute_all_terms(self, term_replacement_dict):
        return self.subs(term_replacement_dict)

