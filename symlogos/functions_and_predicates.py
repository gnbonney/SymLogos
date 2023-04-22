from __future__ import annotations
import sympy
from .expressions_and_terms import LogicalExpression

# higher-order predicates

class Predicate(LogicalExpression):
    def __new__(cls: Type[Predicate], name: Union[    sympy.core.symbol.Symbol, str], *terms) -> "Predicate":
        obj = super().__new__(cls)
        obj.symbol = sympy.Symbol(str(name))  # Convert name to string before creating a sympy.Symbol
        obj.terms = tuple(terms[0]) if len(terms) == 1 and isinstance(terms[0], (list, tuple)) else terms
        return obj

    def __eq__(self, other: "Predicate") -> bool:
        if not isinstance(other, Predicate):
            return False
        return self.symbol == other.symbol and self.terms == other.terms

    def __hash__(self):
        return hash((type(self), self.symbol, self.terms))

    def __str__(self) -> str:
        return f"{self.symbol}({', '.join(map(str, self.terms))})"

    def __repr__(self):
        return f"Predicate('{self.symbol}', {', '.join(map(repr, self.terms))})"
    
    def substitute(self, mapping: Dict[Term, Term]) -> "Predicate":
        new_args = [mapping.get(term, term) for term in self.terms]
        return Predicate(self.symbol, *new_args)

    def substitute_all_terms(self, term_replacement_dict: Dict[Term, Term]) -> "Predicate":
        new_terms = [term_replacement_dict.get(term, term) for term in self.terms]
        new_predicate = Predicate(self.symbol, *new_terms)
        return new_predicate
    
    def evaluate(self, valuation=None):
        if valuation is None:
            return self
        
        if self.symbol in valuation:
            value = valuation[self.symbol]
            if isinstance(value, bool):
                return value

        new_args = [arg.evaluate(valuation) if isinstance(arg, LogicalExpression) else arg for arg in self.terms]
        return Predicate(self.symbol, *new_args)
    
    def match(self, other: "Predicate") -> Dict[Term, Term]:
        if isinstance(other, Predicate):
            if self.symbol == other.symbol and len(self.terms) == len(other.terms):
                bindings = {}
                for t1, t2 in zip(self.terms, other.terms):
                    b = t1.match(t2)
                    if b is None:
                        print(f"Matching failed for: self: {self}, other: {other}, terms: {t1}, {t2}")
                        return None
                    print(f"Matched terms: {t1}, {t2}, binding: {b}")
                    bindings.update(b)
                print(f"Match successful: self: {self}, other: {other}, bindings: {bindings}")
                return bindings
            else:
                print(f"Matching failed due to different symbol or term count: self: {self}, other: {other}")
                return None
        else:
            print(f"Matching failed as other is not a Predicate: self: {self}, other: {other}")
            return None

    def is_atomic(self):
        return True
            
    def to_nnf(self) -> "Predicate":
        return self

# high order functions

from sympy import Basic, Symbol
import sympy.core.symbol
from symlogos.expressions_and_terms import Term
from typing import Dict, Optional, Type, Union

class HigherOrderFunction(Basic):
    def __new__(cls: Type[HigherOrderFunction], name: str, arg_function: Optional[HigherOrderFunction]=None, return_function: Optional[Union[Predicate, HigherOrderFunction]]=None, *args) -> "HigherOrderFunction":
        obj = super().__new__(cls)
        obj._name = Symbol(name)
        obj._arg_function = arg_function
        obj._return_function = return_function
        obj._args = args
        return obj

    @property
    def name(self) ->     sympy.core.symbol.Symbol:
        return self._name

    @property
    def arg_function(self):
        return self._arg_function

    @arg_function.setter
    def arg_function(self, value):
        self._arg_function = value

    @property
    def return_function(self):
        return self._return_function

    @return_function.setter
    def return_function(self, value):
        self._return_function = value

    def __str__(self) -> str:
        arg_str = f"({', '.join(map(str, self.args))})" if self.args else ""
        if self.arg_function and self.return_function:
            return f"{self.name}({self.arg_function}) -> {self.return_function}{arg_str}"
        elif self.arg_function:
            return f"{self.name}({self.arg_function}{arg_str})"
        elif self.return_function:
            return f"{self.name} -> {self.return_function}{arg_str}"
        else:
            return f"{self.name}{arg_str}"

    def __repr__(self) -> str:
        return f"HigherOrderFunction('{self.name}', {repr(self.arg_function)}, {repr(self.return_function)})"
    
    def match(self, expr):
        if isinstance(expr, HigherOrderFunction) and self.name == expr.name:
            # check argument function
            if self.arg_function is None or self.arg_function.match(expr.arg_function):
                # check return function
                if self.return_function is None or self.return_function.match(expr.return_function):
                    # match arguments
                    if len(self.args) != len(expr.args):
                        print(f"Matching failed due to different argument count: self: {self}, expr: {expr}")
                        return None
                    substitutions = {}
                    for i in range(len(self.args)):
                        arg1 = self.args[i]
                        arg2 = expr.args[i]
                        result = arg1.match(arg2)
                        if result is None:
                            print(f"Matching failed for arguments: self: {self}, expr: {expr}, args: {arg1}, {arg2}")
                            return None
                        print(f"Matched arguments: {arg1}, {arg2}, binding: {result}")
                        substitutions.update(result)
                    print(f"Match successful: self: {self}, expr: {expr}, bindings: {substitutions}")
                    return substitutions
            else:
                print(f"Matching failed due to argument or return function mismatch: self: {self}, expr: {expr}")
                return None
        else:
            print(f"Matching failed as expr is not a HigherOrderFunction or name mismatch: self: {self}, expr: {expr}")
            return None

class FunctionApplication(LogicalExpression):
    def __init__(self, function_symbol: Union[HigherOrderFunction, str], *args) -> None:
        self.function_symbol = function_symbol
        self.arguments = args

    def __str__(self) -> str:
        args_str = ', '.join(str(arg) for arg in self.arguments)
        return f"{self.function_symbol}({args_str})"

    def __eq__(self, other: "FunctionApplication") -> bool:
        if not isinstance(other, FunctionApplication):
            return False
        return self.function_symbol == other.function_symbol and self.arguments == other.arguments
    
    def substitute(self, mapping):
        new_args = tuple(arg.substitute(mapping) for arg in self.arguments)
        return FunctionApplication(self.function_symbol, *new_args)

    def variables(self):
        variables = set()
        for arg in self.arguments:
            variables |= arg.variables()
        return variables

    def match(self, other):
        if isinstance(other, FunctionApplication):
            if self.function_symbol != other.function_symbol or len(self.arguments) != len(other.arguments):
                return None

            match = {}
            for arg_self, arg_other in zip(self.arguments, other.arguments):
                partial_match = arg_self.match(arg_other)
                if partial_match is None:
                    return None

                for key, value in partial_match.items():
                    if key in match and match[key] != value:
                        return None
                    match[key] = value

            return match

        return None


