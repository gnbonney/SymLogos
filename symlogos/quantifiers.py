from .expressions_and_terms import LogicalExpression
from symlogos.expressions_and_terms import Term
from symlogos.functions_and_predicates import Predicate
from symlogos.modal_operators import Necessity
from symlogos.proposition import Proposition
from sympy.core.symbol import Symbol
from typing import Any, Dict, Union

class Forall(LogicalExpression):
    def __init__(self, variable: Union[Symbol, Term, str, Proposition], predicate: Union[Predicate, Necessity, Proposition]) -> None:
        self.variable = variable
        self.predicate = predicate

    def instantiate(self, term):
        return self.predicate.substitute({self.variable: term})

    def __repr__(self):
        return f"∀{self.variable}: {self.predicate}"

    def __eq__(self, other: "Forall") -> bool:
        return isinstance(other, Forall) and self.variable == other.variable and self.predicate == other.predicate

    def __hash__(self):
        return hash((type(self), self.variable, self.predicate))

    def __str__(self) -> str:
        return f"∀{self.variable}: {self.predicate}"

    def __repr__(self):
        return f"Forall({repr(self.variable)}, {repr(self.predicate)})"
    
    def substitute(self, mapping: Dict[Term, Term]) -> "Forall":
        new_bound_variable = mapping.get(self.variable, self.variable)
        new_predicate = self.predicate.substitute(mapping)
        return Forall(new_bound_variable, new_predicate)

    def substitute_all(self, substitutions):
        # Prevent the bound variable from being substituted
        if self.variable in substitutions:
            del substitutions[self.variable]
        
        # Use the default implementation for the remaining substitutions
        return super().substitute_all(substitutions)

    def substitute_all_terms(self, term_replacement_dict: Dict[Any, Any]) -> "Forall":
        new_predicate = self.predicate.substitute_all_terms(term_replacement_dict)
        return Forall(self.variable, new_predicate)

    def match(self, other: "Forall") -> Dict[Any, Any]:
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

    def to_nnf(self) -> "Forall":
        return Forall(self.variable, self.predicate.to_nnf())

class Exists(LogicalExpression):
    def __init__(self, variable: Union[str, Symbol, Term, Proposition], predicate: Union[Predicate, Proposition]) -> None:
        self.variable = variable
        self.predicate = predicate

    def __str__(self) -> str:
        return f"∃{self.variable}: {self.predicate}"

    def __eq__(self, other: "Exists") -> bool:
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

    def match(self, expression: "Exists") -> Dict[Term, Term]:
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

    def to_nnf(self) -> "Exists":
        return Exists(self.variable, self.predicate.to_nnf())
