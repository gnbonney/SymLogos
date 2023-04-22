from __future__ import annotations
from .expressions_and_terms import LogicalExpression, simplify_expression
from symlogos.expressions_and_terms import Term
from typing import Any, Dict, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from symlogos.proposition import Proposition
    from symlogos.modal_operators import Necessity

class Implication(LogicalExpression):
    def __init__(self, antecedent: Union['Proposition', 'Necessity', Term], consequent: Union['Proposition', 'Necessity', Term]) -> None:
        self.antecedent = antecedent
        self.consequent = consequent

    def __hash__(self):
        return hash((type(self), self.antecedent, self.consequent))

    def __eq__(self, other: "Implication") -> bool:
        if isinstance(other, Implication):
            return self.antecedent == other.antecedent and self.consequent == other.consequent
        return False

    def __str__(self) -> str:
        antecedent_str = str(self.antecedent)
        consequent_str = str(self.consequent)
        return f"({antecedent_str} → {consequent_str})"

    def __repr__(self):
        return f"Implication({repr(self.antecedent)}, {repr(self.consequent)})"

    def substitute(self, variable, replacement):
        antecedent_substituted = self.antecedent.substitute(variable, replacement)
        consequent_substituted = self.consequent.substitute(variable, replacement)
        return Implication(antecedent_substituted, consequent_substituted)

    def evaluate(self, valuation=None):
        if valuation is None:
            return self

        antecedent_val = self.antecedent.evaluate(valuation)
        consequent_val = self.consequent.evaluate(valuation)

        if isinstance(antecedent_val, bool) and isinstance(consequent_val, bool):
            return not antecedent_val or consequent_val
        else:
            return Implication(antecedent_val, consequent_val)

    def simplify(self):
        antecedent_simplified = simplify_expression(self.antecedent)
        consequent_simplified = simplify_expression(self.consequent)
    
        if antecedent_simplified == True:
            return consequent_simplified
        if antecedent_simplified == False or consequent_simplified == True:
            return True
        if antecedent_simplified == consequent_simplified:
            return True
    
        return Implication(antecedent_simplified, consequent_simplified)

    def match(self, other: "Implication") -> Dict[Any, Any]:
        if self == other:
            return {}
        return None

    def to_nnf(self) -> "Or":
        negated_antecedent = Not(self.antecedent).to_nnf()
        consequent_nnf = self.consequent.to_nnf()
        return Or(negated_antecedent, consequent_nnf)


class And(LogicalExpression):
    def __init__(self, left: Any, right: Union[And, Term, Or, 'Proposition', Not]) -> None:
        self.left = left
        self.right = right

    def __hash__(self):
        return hash((type(self), self.left, self.right))

    def __str__(self) -> str:
        left_str = str(self.left)
        right_str = str(self.right)
        return f"({left_str} ∧ {right_str})"

    def __repr__(self):
        return f"And({repr(self.left)}, {repr(self.right)})"
    
    def substitute(self, variable: 'Proposition', replacement: 'Proposition') -> "And":
        left_substituted = self.left.substitute(variable, replacement)
        right_substituted = self.right.substitute(variable, replacement)
        return And(left_substituted, right_substituted)

    def substitute_all_terms(self, term_replacement_dict: Dict[Any, Any]) -> "And":
        left_substituted = self.left.substitute_all_terms(term_replacement_dict)
        right_substituted = self.right.substitute_all_terms(term_replacement_dict)
        return And(left_substituted, right_substituted)

    def evaluate(self, valuation=None):
        if valuation is None:
            return self
        
        left_val = self.left.evaluate(valuation)
        right_val = self.right.evaluate(valuation)

        if isinstance(left_val, bool) and isinstance(right_val, bool):
            return left_val and right_val
        else:
            return And(left_val, right_val)

    def __eq__(self, other: "And") -> bool:
        if isinstance(other, And):
            return self.left == other.left and self.right == other.right
        return False
        
    def simplify(self) -> Union['Proposition', bool, And]:
        left_simplified = simplify_expression(self.left)
        right_simplified = simplify_expression(self.right)

        if left_simplified == True:
            return right_simplified
        if right_simplified == True:
            return left_simplified
        if left_simplified == False or right_simplified == False:
            return False

        if isinstance(left_simplified, Not) and isinstance(left_simplified.expr, Not):
            left_simplified = left_simplified.expr.expr
        if isinstance(right_simplified, Not) and isinstance(right_simplified.expr, Not):
            right_simplified = right_simplified.expr.expr

        if left_simplified == self.left and right_simplified == self.right:
            return self

        return And(left_simplified, right_simplified)

    def match(self, other: "And", bindings: None=None) -> Dict[Any, Any]:
        if bindings is None:
            bindings = {}
            
        if isinstance(other, And):
            left_match = self.left.match(other.left, bindings)
            right_match = self.right.match(other.right, bindings)
            
            if left_match is None or right_match is None:
                return None
            
            new_bindings = dict(bindings)
            new_bindings.update(left_match)
            new_bindings.update(right_match)
            return new_bindings

        if isinstance(other, LogicalExpression):
            return bindings

        return None

    def to_nnf(self) -> "And":
        return And(*(arg.to_nnf() for arg in self.args))


class Or(LogicalExpression):
    def __init__(self, left: Union['Proposition', And, Or, Not], right: Union['Proposition', Or, Not, And]) -> None:
        self.left = left
        self.right = right

    def __hash__(self):
        return hash((type(self), self.left, self.right))

    def __repr__(self):
        return f"({self.left} ∨ {self.right})"

    def __eq__(self, other: "Or") -> bool:
        if not isinstance(other, Or):
            return False
        return self.left == other.left and self.right == other.right

    def variables(self):
        return self.left.variables().union(self.right.variables())

    def substitute_all_terms(self, term_replacement_dict: Dict[Any, Any]) -> "Or":
        new_left = self.left.substitute_all_terms(term_replacement_dict)
        new_right = self.right.substitute_all_terms(term_replacement_dict)
        return Or(new_left, new_right)

    def match(self, other: "Or", bindings: None=None) -> Dict[Any, Any]:
        if bindings is None:
            bindings = {}

        if isinstance(other, Or):
            left_match = self.left.match(other.left, bindings)
            if left_match is not None:
                right_match = self.right.match(other.right, left_match)
                if right_match is not None:
                    return right_match
        return None

    def to_nnf(self) -> "Or":
        return Or(*(arg.to_nnf() for arg in self.args))

class Not(LogicalExpression):
    def __init__(self, expr: Union[And, bool, Or, 'Proposition', Not]) -> None:
        super().__init__()
        self.expr = expr

    def __eq__(self, other: "Not") -> bool:
        if isinstance(other, Not):
            return self.expr == other.expr
        return False

    def __hash__(self):
        return hash((type(self), self.expr))

    def __str__(self) -> str:
        return f"¬{str(self.expr)}"

    def __repr__(self):
        return f"Not({repr(self.expr)})"
    
    def substitute(self, variable: 'Proposition', replacement: 'Proposition') -> "Not":
        return Not(self.expr.substitute(variable, replacement))

    def substitute_all_terms(self, term_replacement_dict: Dict[Any, Any]) -> "Not":
        new_expr = self.expr.substitute_all_terms(term_replacement_dict)  # Change this line
        return Not(new_expr)
    
    def evaluate(self, valuation=None):
        if valuation is None:
            return self
        
        expr_val = self.expr.evaluate(valuation)

        if isinstance(expr_val, bool):
            return not expr_val
        else:
            return Not(expr_val)
    
    def simplify(self) -> Union['Proposition', bool, Not]:
        simplified_inner = simplify_expression(self.expr)

        if isinstance(simplified_inner, Not):
            return simplified_inner.expr

        if simplified_inner == True:
            return False

        if simplified_inner == False:
            return True

        return Not(simplified_inner)

    def __eq__(self, other: "Not") -> bool:
        if isinstance(other, Not):
            return self.expr == other.expr
        return False
    
    def match(self, other: "Not") -> Dict[Any, Any]:
        if isinstance(other, Not):
            print(f"Matching Not: self: {self}, other: {other}")
            result = self.expr.match(other.expr)
            print(f"Match result: {result}")
            return result
        else:
            print(f"Matching without Not: self: {self}, other: {other}")
            result = self.expr.match(other)
            print(f"Match result: {result}")
            return result

    def to_nnf(self) -> "Not":
        inner = self.expr
        if inner.is_atomic():
            return self
        if isinstance(inner, And):
            return Or(*(Not(expr).to_nnf() for expr in inner.expr))
        if isinstance(inner, Or):
            return And(*(Not(expr).to_nnf() for expr in inner.expr))
        if isinstance(inner, Not):
            return inner.expr.to_nnf()