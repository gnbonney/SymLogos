from sympy import symbols
from sympy.logic import *

def simplify_expression(expr):
    if isinstance(expr, Expression):
        return expr.simplify()
    return expr

# Define basic classes for propositional variables and modal operators.

class Expression:
    def substitute(self, substitution):
        return self

    def evaluate(self, assignment):
        return self

    def simplify(self):
        return self

class Proposition(Expression):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Proposition('{self.name}')"

    def not_(self):
        return Not(self)

    def box(self):
        return Necessity(self)

    def diamond(self):
        return Possibility(self)

    def substitute(self, variable, replacement):
        if self == variable:
            return replacement
        else:
            return self

    def evaluate(self, assignment):
        if self.name in assignment:
            return assignment[self.name]
        else:
            raise ValueError(f"Assignment for proposition '{self.name}' not found.")



class And(Expression):
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

        if left_simplified == self.left and right_simplified == self.right:
            return self

        return And(left_simplified, right_simplified)

class Not(Expression):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        return f"¬{self.formula}"

    def __repr__(self):
        return f"Not({repr(self.formula)})"
    
    def substitute(self, variable, replacement):
        return Not(self.formula.substitute(variable, replacement))
    
    def evaluate(self, valuation=None):
        if valuation is None:
            return self
        
        formula_val = self.formula.evaluate(valuation)

        if isinstance(formula_val, bool):
            return not formula_val
        else:
            return Not(formula_val)
    
    def simplify(self):
        simplified_inner = simplify_expression(self.formula)

        if isinstance(simplified_inner, Not):
            return simplified_inner.formula

        if simplified_inner == True:
            return False

        if simplified_inner == False:
            return True

        return Not(simplified_inner)

    def __eq__(self, other):
        if isinstance(other, Not):
            return self.formula == other.formula
        return False


class Necessity(Expression):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        return f"□{self.formula}"

    def __repr__(self):
        return f"Necessity({repr(self.formula)})"
    
    def simplify(self):
        formula_simplified = simplify_expression(self.formula)

        if formula_simplified == True:
            return True

        if formula_simplified == False:
            return False

        return Necessity(formula_simplified)


class Possibility(Expression):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        return f"◇{self.formula}"

    def __repr__(self):
        return f"Possibility({repr(self.formula)})"

    def simplify(self):
        formula_simplified = simplify_expression(self.formula)

        if formula_simplified == True:
            return True

        if formula_simplified == False:
            return False

        return Possibility(formula_simplified)

# Add classes for higher-order predicates

class Predicate(Expression):
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __str__(self):
        return f"{self.name}({', '.join(map(str, self.args))})"

    def __repr__(self):
        return f"Predicate('{self.name}', {', '.join(map(repr, self.args))})"
    
    def substitute(self, mapping):
        new_args = [arg.substitute(mapping) if isinstance(arg, Expression) else arg for arg in self.args]
        return Predicate(self.name, *new_args)
    
    def evaluate(self, valuation=None):
        if valuation is None:
            return self
        
        if self.name in valuation:
            value = valuation[self.name]
            if isinstance(value, bool):
                return value

        new_args = [arg.evaluate(valuation) if isinstance(arg, Expression) else arg for arg in self.args]
        return Predicate(self.name, *new_args)


class Forall(Expression):
    def __init__(self, variable, formula):
        self.variable = variable
        self.formula = formula

    def __str__(self):
        return f"∀{self.variable}: {self.formula}"

    def __repr__(self):
        return f"Forall({repr(self.variable)}, {repr(self.formula)})"
    
    def substitute(self, mapping):
        if self.variable in mapping:
            raise ValueError(f"Cannot substitute bound variable '{self.variable}'")
        new_formula = self.formula.substitute(mapping)
        return Forall(self.variable, new_formula)


class Exists(Expression):
    def __init__(self, variable, formula):
        self.variable = variable
        self.formula = formula

    def __str__(self):
        return f"∃{self.variable}: {self.formula}"

    def __repr__(self):
        return f"Exists({repr(self.variable)}, {repr(self.formula)})"

    def substitute(self, mapping):
        if self.variable in mapping:
            raise ValueError(f"Cannot substitute bound variable '{self.variable}'")
        new_formula = self.formula.substitute(mapping)
        return Exists(self.variable, new_formula)

# Add a class for high order functions

class HigherOrderFunction(Expression):
    def __init__(self, name, arg_function=None, return_function=None, *args):
        self.name = name
        self.arg_function = arg_function
        self.return_function = return_function
        self.args = args

    def __call__(self, *args):
        return Predicate(self.name, *args)

    def __str__(self):
        arg_str = f"({', '.join(map(str, self.args))})" if self.args else ""
        if self.arg_function and self.return_function:
            return f"{self.name}({self.arg_function}) -> {self.return_function}{arg_str}"
        elif self.arg_function:
            return f"{self.name}({self.arg_function}{arg_str})"
        elif self.return_function:
            return f"{self.name} -> {self.return_function}{arg_str}"
        else:
            return f"{self.name}{arg_str}"

    def __repr__(self):
        return f"HigherOrderFunction('{self.name}', {repr(self.arg_function)}, {repr(self.return_function)})"
# Add functions for defining axioms, proving theorems, and checking consistency and validity.

def define_axiom():
    pass

def prove_theorem():
    pass

def check_consistency():
    pass

def check_validity():
    pass

# Example usage:

if __name__ == "__main__":
    p = Proposition("p")
    not_p = p.neg()
    box_p = p.box()
    diamond_p = p.diamond()

    print(not_p)
    print(box_p)
    print(diamond_p)

    x, y = symbols("x y")
    Px = Predicate("P", x)
    Py = Predicate("P", y)
    forall_px = Forall(x, Px)
    exists_py = Exists(y, Py)
    
    print(forall_px)
    print(exists_py)

    F = HigherOrderFunction("F")
    f_of_p = F(p)
    print(f_of_p)