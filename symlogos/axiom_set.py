class AxiomSet:
    def __init__(self):
        self.axioms = set()

    def add_axiom(self, axiom):
        self.axioms.add(axiom)

    def remove_axiom(self, axiom):
        if axiom in self.axioms:
            self.axioms.remove(axiom)

    def __iter__(self):
        return iter(self.axioms)

    def __len__(self):
        return len(self.axioms)

    def __contains__(self, axiom):
        return axiom in self.axioms

    def __repr__(self):
        return f"AxiomSet({', '.join(map(str, self.axioms))})"