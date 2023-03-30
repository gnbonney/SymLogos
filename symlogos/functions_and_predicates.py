from .expressions_and_terms import Expression

# higher-order predicates

class Predicate(Expression):
    def __init__(self, symbol, *terms):
        self.symbol = symbol
        self.terms = terms

    def __eq__(self, other):
        if not isinstance(other, Predicate):
            return False
        return self.symbol == other.symbol and self.terms == other.terms

    def __hash__(self):
        return hash((type(self), self.symbol, self.terms))

    def __hash__(self):
        return hash((self.symbol, self.terms))

    def __str__(self):
        return f"{self.symbol}({', '.join(map(str, self.terms))})"

    def __repr__(self):
        return f"Predicate('{self.symbol}', {', '.join(map(repr, self.terms))})"
    
    def substitute(self, mapping):
        new_args = [arg.substitute(mapping) if isinstance(arg, Expression) else arg for arg in self.terms]
        return Predicate(self.symbol, *new_args)
    
    def evaluate(self, valuation=None):
        if valuation is None:
            return self
        
        if self.symbol in valuation:
            value = valuation[self.symbol]
            if isinstance(value, bool):
                return value

        new_args = [arg.evaluate(valuation) if isinstance(arg, Expression) else arg for arg in self.terms]
        return Predicate(self.symbol, *new_args)
    
    def match(self, other):
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

# high order functions

class HigherOrderFunction(Expression):
    def __init__(self, name, arg_function=None, return_function=None, *args):
        self.name = name
        self.arg_function = arg_function
        self.return_function = return_function
        self.args = args

    def __eq__(self, other):
        if isinstance(other, HigherOrderFunction):
            return self.name == other.name
        return False

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

