from .expressions_and_terms import Expression
class Rule:
    def __init__(self, name, premises, conclusion):
        self.name = name
        self.premises = premises
        self.conclusion = conclusion

    def __str__(self):
        premises_str = ", ".join(map(str, self.premises))
        return f"{self.name}: {premises_str} ⊢ {self.conclusion}"

    def __repr__(self):
        premises_repr = ", ".join(map(repr, self.premises))
        return f"Rule('{self.name}', [{premises_repr}], {repr(self.conclusion)})"

    def apply(self, *args):
        if len(args) != len(self.premises):
            raise ValueError("Wrong number of arguments")

        match_dicts = []
        for premise, arg in zip(self.premises, args):
            current_match = premise.match(arg)
            if current_match is None:
                return None
            match_dicts.append(current_match)

        match_dict = {}
        for d in match_dicts:
            match_dict.update(d)

        result = self.conclusion.substitute_all_terms(match_dict)  # Change this line
        return result

def check_consistency():
    pass

def check_validity():
    pass