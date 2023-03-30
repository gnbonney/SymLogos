from .expressions_and_terms import Expression

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
    
    def substitute(self, variable, replacement):
        mapping = {variable: replacement}
        new_predicate = self.predicate.substitute(mapping)
        new_variable = replacement if self.variable == variable else self.variable
        return Forall(new_variable, new_predicate)

    def match(self, other):
        if isinstance(other, Forall):
            variable_match = self.variable.match(other.variable)
            predicate_match = self.predicate.match(other.predicate)
            print(f"Forall match: self: {self}, other: {other}, variable_match: {variable_match}, predicate_match: {predicate_match}")
            if variable_match is not None and predicate_match is not None:
                bindings = {}
                bindings.update(variable_match)
                bindings.update(predicate_match)
                return bindings
        return None

    def substitute_all(self, substitutions):
        # Prevent the bound variable from being substituted
        if self.variable in substitutions:
            del substitutions[self.variable]
        
        # Use the default implementation for the remaining substitutions
        return super().substitute_all(substitutions)

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
            predicate_match = self.predicate.match(expression.predicate)
            if predicate_match is not None:
                print(f"Match successful: self: {self}, expression: {expression}, substitutions: {predicate_match}")
                return predicate_match
            else:
                print(f"Matching failed for predicates: self.predicate: {self.predicate}, expression.predicate: {expression.predicate}")
        else:
            print(f"Matching failed for different types: self: {self}, expression: {expression}")
        return None
