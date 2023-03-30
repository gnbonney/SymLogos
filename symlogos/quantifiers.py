from .expression import Expression

class Forall(Expression):
    def __init__(self, variable, predicate):
        self.variable = variable
        self.predicate = predicate

    def __repr__(self):
        return f"∀{self.variable}: {self.predicate}"

    def __eq__(self, other):
        return isinstance(other, Forall) and self.variable == other.variable and self.predicate == other.predicate

    def __hash__(self):
        return hash((type(self), self.variable, self.predicate))

    def __str__(self):
        return f"∀{self.variable}: {self.predicate}"

    def __repr__(self):
        return f"Forall({repr(self.variable)}, {repr(self.predicate)})"
    
    def substitute(self, mapping):
        if self.variable in mapping:
            raise ValueError(f"Cannot substitute bound variable '{self.variable}'")
        new_predicate = self.predicate.substitute(mapping)
        return Forall(self.variable, new_predicate)

    def match(self, expr):
        if isinstance(expr, Forall):
            if self.variable.match(expr.variable) and self.predicate.match(expr.predicate):
                return {}
        return None

class Exists(Expression):
    def __init__(self, variable, predicate):
        self.variable = variable
        self.predicate = predicate

    def __str__(self):
        return f"∃{self.variable}: {self.predicate}"

    def __eq__(self, other):
        if not isinstance(other, Exists):
            return False
        return self.variable == other.variable and self.predicate == other.predicate

    def __hash__(self):
        return hash((type(self), self.variable, self.predicate))

    def __repr__(self):
        return f"Exists({repr(self.variable)}, {repr(self.predicate)})"

    def substitute(self, mapping):
        if self.variable in mapping:
            raise ValueError(f"Cannot substitute bound variable '{self.variable}'")
        new_expr = self.predicate.substitute(mapping)
        return Exists(self.variable, new_expr)

    def match(self, expression):
        if isinstance(expression, Exists):
            substitutions = self.variable.match(expression.variable)
            if substitutions is not None:
                new_predicate = self.predicate.substitute(substitutions)
                if new_predicate == expression.predicate:
                    return substitutions
        return None