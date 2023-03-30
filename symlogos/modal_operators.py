from .expression import Expression, simplify_expression

class Necessity(Expression):
    def __init__(self, expr):
        self.expr = expr

    def __eq__(self, other):
        if isinstance(other, Necessity):
            return self.expr == other.expr
        return False

    def __str__(self):
        return f"□{self.expr}"

    def __repr__(self):
        return f"Necessity({repr(self.expr)})"
    
    def simplify(self):
        expr_simplified = simplify_expression(self.expr)

        if expr_simplified == True:
            return True

        if expr_simplified == False:
            return False

        return Necessity(expr_simplified)

    def match(self, other):
        if isinstance(other, Necessity):
            return self.expr.match(other.expr)
        else:
            return self.expr.match(other)


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
            return self.expr.match(other.expr)
        else:
            return self.expr.match(other)