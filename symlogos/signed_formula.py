class SignedFormula:
    def __init__(self, sign, formula):
        if sign not in ('T', 'F'):
            raise ValueError("Sign must be either 'T' or 'F'")
        self.sign = sign
        self.formula = formula

    def __str__(self):
        return f"{self.sign} {self.formula}"

    def __eq__(self, other):
        if not isinstance(other, SignedFormula):
            return False
        return self.sign == other.sign and self.formula == other.formula

    def __hash__(self):
        return hash((type(self), self.sign, self.formula))

    def is_positive(self):
        return self.sign == 'T'

    def is_negative(self):
        return self.sign == 'F'
