from abc import ABC, abstractmethod

def simplify_expression(expr):
    if isinstance(expr, Expression):
        return expr.simplify()
    return expr

class Expression(ABC):
    def substitute(self, substitution):
        return self

    def evaluate(self, assignment):
        return self

    def simplify(self):
        return self

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass
    
    @abstractmethod
    def match(self, other):
        pass

    def substitute_all(self, substitutions):
        new_attributes = {}
        for attr, value in self.__dict__.items():
            if isinstance(value, Expression):
                new_attributes[attr] = value.substitute_all(substitutions)
            elif isinstance(value, Term) and value in substitutions:
                new_attributes[attr] = substitutions[value]
            elif isinstance(value, tuple):  
                new_attributes[attr] = tuple(v.substitute_all(substitutions) if isinstance(v, Expression) else substitutions.get(v, v) for v in value)
            else:
                new_attributes[attr] = value
        result = self.__class__(*new_attributes.values())
        return result

class Term(Expression):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Term):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash((type(self), self.name))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Term('{self.name}')"

    def substitute(self, mapping):
        if self in mapping:
            return mapping[self]
        return self

    def evaluate(self, assignment):
        if self.name in assignment:
            return assignment[self.name]
        else:
            raise ValueError(f"Assignment for term '{self.name}' not found.")

    def match(self, other):
        if isinstance(other, Term):
            if self.name == other.name:
                print(f"Match successful: self: {self}, other: {other}")
                return {}
            else:
                print(f"Matching failed for terms: self: {self}, other: {other}")
                return None
        else:
            print(f"Matching failed for different types: self: {self}, other: {other}")
            return None