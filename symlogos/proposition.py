from __future__ import annotations
import sympy
from .expressions_and_terms import LogicalExpression
from typing import Any, Dict, Type, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from symlogos.connectives import Not

class Proposition(LogicalExpression):
    def __new__(cls: Type[Proposition], name: str) -> "Proposition":
        obj = super().__new__(cls)
        obj.name = sympy.Symbol(name)
        return obj

    def __eq__(self, other: Union[bool, Proposition, Not]) -> bool:
        if isinstance(other, Proposition):
            return self.name == other.name
        return False

    def __hash__(self) -> int:
        return hash((type(self), self.name))

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self):
        return f"Proposition('{self.name}')"

    def match(self, other: "Proposition", bindings: None=None) -> Dict[Any, Any]:
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

    def evaluate(self, assignment: Dict[Proposition, bool]) -> bool:
        return assignment.get(self, self)

    def simplify(self) -> "Proposition":
        return self

    def substitute(self, variable: "Proposition", replacement: "Proposition") -> "Proposition":
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

    def substitute_all_terms(self, term_replacement_dict: Dict[Any, Any]) -> "Proposition":
        return self.subs(term_replacement_dict)

    def is_atomic(self) -> bool:
        return True
