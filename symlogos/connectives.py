from .expressions_and_terms import LogicalExpression, simplify_expression

class Implication(LogicalExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(other, Implication):
            return self.left == other.left and self.right == other.right
        return False

    def __str__(self):
        left_str = str(self.left)
        right_str = str(self.right)
        return f"({left_str} → {right_str})"

    def __repr__(self):
        return f"Implication({repr(self.left)}, {repr(self.right)})"

    def substitute(self, variable, replacement):
        left_substituted = self.left.substitute(variable, replacement)
        right_substituted = self.right.substitute(variable, replacement)
        return Implication(left_substituted, right_substituted)

    def evaluate(self, valuation=None):
        if valuation is None:
            return self

        left_val = self.left.evaluate(valuation)
        right_val = self.right.evaluate(valuation)

        if isinstance(left_val, bool) and isinstance(right_val, bool):
            return not left_val or right_val
        else:
            return Implication(left_val, right_val)

    def simplify(self):
        left_simplified = simplify_expression(self.left)
        right_simplified = simplify_expression(self.right)
    
        if left_simplified == True:
            return right_simplified
        if left_simplified == False or right_simplified == True:
            return True
        if left_simplified == right_simplified:
            return True
    
        return Implication(left_simplified, right_simplified)

    def match(self, other):
        if self == other:
            return {}
        return None

class And(LogicalExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        left_str = str(self.left)
        right_str = str(self.right)
        return f"({left_str} ∧ {right_str})"

    def __repr__(self):
        return f"And({repr(self.left)}, {repr(self.right)})"
    
    def substitute(self, variable, replacement):
        left_substituted = self.left.substitute(variable, replacement)
        right_substituted = self.right.substitute(variable, replacement)
        return And(left_substituted, right_substituted)

    def substitute_all_terms(self, term_replacement_dict):
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

    def __eq__(self, other):
        if isinstance(other, And):
            return self.left == other.left and self.right == other.right
        return False
        
    def simplify(self):
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

    def match(self, other, bindings=None):
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


class Or(LogicalExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} ∨ {self.right})"

    def __eq__(self, other):
        if not isinstance(other, Or):
            return False
        return self.left == other.left and self.right == other.right

    def variables(self):
        return self.left.variables().union(self.right.variables())

    def substitute_all_terms(self, term_replacement_dict):
        new_left = self.left.substitute_all_terms(term_replacement_dict)
        new_right = self.right.substitute_all_terms(term_replacement_dict)
        return Or(new_left, new_right)

    def match(self, other, bindings=None):
        if bindings is None:
            bindings = {}

        if isinstance(other, Or):
            left_match = self.left.match(other.left, bindings)
            if left_match is not None:
                right_match = self.right.match(other.right, left_match)
                if right_match is not None:
                    return right_match
        return None

class Not(LogicalExpression):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr

    def __eq__(self, other):
        if isinstance(other, Not):
            return self.expr == other.expr
        return False

    def __hash__(self):
        return hash((type(self), self.expr))

    def __str__(self):
        return f"¬{str(self.expr)}"

    def __repr__(self):
        return f"Not({repr(self.expr)})"
    
    def substitute(self, variable, replacement):
        return Not(self.expr.substitute(variable, replacement))

    def substitute_all_terms(self, term_replacement_dict):
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
    
    def simplify(self):
        simplified_inner = simplify_expression(self.expr)

        if isinstance(simplified_inner, Not):
            return simplified_inner.expr

        if simplified_inner == True:
            return False

        if simplified_inner == False:
            return True

        return Not(simplified_inner)

    def __eq__(self, other):
        if isinstance(other, Not):
            return self.expr == other.expr
        return False
    
    def match(self, other):
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