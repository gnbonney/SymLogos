from .expressions_and_terms import Expression, simplify_expression

class Necessity(Expression):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return f"□{self.expr}"

    def __eq__(self, other):
        if not isinstance(other, Necessity):
            return False
        return self.expr == other.expr

    def __hash__(self):
        return hash((type(self), self.expr))

    def __repr__(self):
        return f"Necessity({repr(self.expr)})"

    def simplify(self):
        expr_simplified = simplify_expression(self.expr)

        if expr_simplified == True:
            return True

        if expr_simplified == False:
            return False

        return Necessity(expr_simplified)

    def substitute(self, mapping):
        new_expr = self.expr.substitute(mapping)
        return Necessity(new_expr)

    def substitute_all_terms(self, term_replacement_dict):
        new_expr = self.expr.substitute_all_terms(term_replacement_dict)
        return Necessity(new_expr)

    def match(self, expression):
        if isinstance(expression, Necessity):
            match_result = self.expr.match(expression.expr)
            if match_result is not None:
                return match_result
        return None



class Possibility(Expression):
    def __init__(self, expr):
        self.expr = expr

    def __eq__(self, other):
        if isinstance(other, Possibility):
            return self.expr == other.expr
        return False

    def __hash__(self):
        return hash((type(self), self.expr))

    def __str__(self):
        return f"◇{self.expr}"

    def __repr__(self):
        return f"Possibility({repr(self.expr)})"

    def simplify(self):
        expr_simplified = simplify_expression(self.expr)

        if expr_simplified == True:
            return True

        if expr_simplified == False:
            return False

        return Possibility(expr_simplified)

    def match(self, other):
        if isinstance(other, Possibility):
            match_result = self.expr.match(other.expr)
            if match_result is None:
                print(f"Matching failed for expressions: self: {self}, other: {other}")
            else:
                print(f"Match successful: self: {self}, other: {other}, bindings: {match_result}")
            return match_result
        else:
            match_result = self.expr.match(other)
            if match_result is None:
                print(f"Matching failed for expressions with different types: self: {self}, other: {other}")
            else:
                print(f"Match successful: self: {self}, other: {other}, bindings: {match_result}")
            return match_result
