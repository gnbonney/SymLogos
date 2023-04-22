from symlogos.proposition import Proposition

class AxiomSet:
    def __init__(self) -> None:
        self.axioms = set()

    def add_axiom(self, axiom: Proposition) -> None:
        self.axioms.add(axiom)

    def remove_axiom(self, axiom: Proposition) -> None:
        if axiom in self.axioms:
            self.axioms.remove(axiom)

    def __iter__(self):
        return iter(self.axioms)

    def __len__(self) -> int:
        return len(self.axioms)

    def __contains__(self, axiom: Proposition) -> bool:
        return axiom in self.axioms

    def __repr__(self) -> str:
        return f"AxiomSet({', '.join(map(str, self.axioms))})"