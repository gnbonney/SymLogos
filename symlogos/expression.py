from abc import ABC, abstractmethod

def simplify_expression(expr):
    if isinstance(expr, Expression):
        return expr.simplify()
    return expr

class Expression(ABC):
    def substitute(self, substitution):
        return self

    def evaluate(self, assignment):
        return self

    def simplify(self):
        return self

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass
    
    @abstractmethod
    def match(self, other):
        pass