# Module: main

## Functions:

- `demonstrate_propositions() -> unknown`

- `demonstrate_predicates_quantifiers() -> unknown`

- `demonstrate_function_application() -> unknown`

- `demonstrate_implications() -> unknown`

---

# Module: utils.project_analyzer

## Functions:

- `analyze_module(file_path: unknown) -> unknown`

- `analyze_project(project_root: unknown) -> unknown`

- `print_summary(summary: unknown) -> unknown`

---

# Module: utils.automate_monkeytype

## Functions:

- `discover_modules(project_root: unknown) -> unknown`

- `main(project_root: unknown) -> unknown`

---

# Module: symlogos.proposition

## Classes:

### Proposition

#### Methods:

- `__new__(cls: Type[Proposition], name: str) -> 'Proposition'`

- `__eq__(self: unknown, other: Union[bool, Proposition, Not]) -> bool`

- `__hash__(self: unknown) -> int`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> unknown`

- `match(self: unknown, other: 'Proposition', bindings: None) -> Dict[Any, Any]`

- `evaluate(self: unknown, assignment: Dict[Proposition, bool]) -> bool`

- `simplify(self: unknown) -> 'Proposition'`

- `substitute(self: unknown, variable: 'Proposition', replacement: 'Proposition') -> 'Proposition'`

- `substitute_all(self: unknown, substitutions: unknown) -> unknown`

- `substitute_all_terms(self: unknown, term_replacement_dict: Dict[Any, Any]) -> 'Proposition'`

- `is_atomic(self: unknown) -> bool`

---

# Module: symlogos.quantifiers

## Classes:

### Forall

#### Methods:

- `__init__(self: unknown, variable: Union[Symbol, Term, str, Proposition], predicate: Union[Predicate, Necessity, Proposition]) -> None`

- `instantiate(self: unknown, term: unknown) -> unknown`

- `__repr__(self: unknown) -> unknown`

- `__eq__(self: unknown, other: 'Forall') -> bool`

- `__hash__(self: unknown) -> unknown`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> unknown`

- `substitute(self: unknown, mapping: Dict[Term, Term]) -> 'Forall'`

- `substitute_all(self: unknown, substitutions: unknown) -> unknown`

- `substitute_all_terms(self: unknown, term_replacement_dict: Dict[Any, Any]) -> 'Forall'`

- `match(self: unknown, other: 'Forall') -> Dict[Any, Any]`

- `to_nnf(self: unknown) -> 'Forall'`

### Exists

#### Methods:

- `__init__(self: unknown, variable: Union[str, Symbol, Term, Proposition], predicate: Union[Predicate, Proposition]) -> None`

- `__str__(self: unknown) -> str`

- `__eq__(self: unknown, other: 'Exists') -> bool`

- `__hash__(self: unknown) -> unknown`

- `__repr__(self: unknown) -> unknown`

- `substitute(self: unknown, mapping: unknown) -> unknown`

- `match(self: unknown, expression: 'Exists') -> Dict[Term, Term]`

- `to_nnf(self: unknown) -> 'Exists'`

---

# Module: symlogos.signed_formula

## Classes:

### SignedFormula

#### Methods:

- `__init__(self: unknown, sign: str, formula: Basic) -> None`

- `__str__(self: unknown) -> unknown`

- `__eq__(self: unknown, other: 'SignedFormula') -> bool`

- `__hash__(self: unknown) -> unknown`

- `is_positive(self: unknown) -> bool`

- `is_negative(self: unknown) -> unknown`

---

# Module: symlogos.expressions_and_terms

## Classes:

### CombinedMeta

### LogicalExpression

#### Methods:

- `__eq__(self: unknown, other: unknown) -> unknown`

- `__hash__(self: unknown) -> unknown`

- `match(self: unknown, other: unknown) -> unknown`

- `substitute(self: unknown, mapping: unknown) -> unknown`

- `substitute_all(self: unknown, substitutions: unknown) -> unknown`

- `substitute_all_terms(self: unknown, term_replacement_dict: Dict[Any, Any]) -> Union['Possibility', 'Implication']`

- `evaluate(self: unknown, assignment: unknown) -> unknown`

- `is_atomic(self: unknown) -> unknown`

- `to_nnf(self: unknown) -> 'Proposition'`

### Term

#### Methods:

- `__new__(cls: Type[Term], name: str) -> 'Term'`

- `__eq__(self: unknown, other: 'Term') -> bool`

- `__hash__(self: unknown) -> int`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> str`

- `substitute(self: unknown, mapping: unknown) -> unknown`

- `evaluate(self: unknown, assignment: unknown) -> unknown`

- `match(self: unknown, other: 'Term') -> Dict[Term, Term]`

- `is_variable(self: unknown) -> bool`

## Functions:

- `simplify_expression(expr: Union['Not', bool, 'Proposition']) -> Union['Not', bool, 'Proposition']`

---

# Module: symlogos.modal_operators

## Classes:

### Necessity

#### Methods:

- `__init__(self: unknown, expr: Any) -> None`

- `__str__(self: unknown) -> str`

- `__eq__(self: unknown, other: 'Necessity') -> bool`

- `__hash__(self: unknown) -> unknown`

- `__repr__(self: unknown) -> unknown`

- `simplify(self: unknown) -> bool`

- `substitute(self: unknown, mapping: unknown) -> unknown`

- `substitute_all_terms(self: unknown, term_replacement_dict: Dict[Any, Any]) -> 'Necessity'`

- `match(self: unknown, expression: 'Necessity') -> Dict[Any, Any]`

### Possibility

#### Methods:

- `__init__(self: unknown, expr: Union[bool, And, Proposition]) -> None`

- `__eq__(self: unknown, other: 'Possibility') -> bool`

- `__hash__(self: unknown) -> unknown`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> unknown`

- `simplify(self: unknown) -> bool`

- `match(self: unknown, other: 'Possibility') -> Dict[Any, Any]`

---

# Module: symlogos.modal_logic

## Classes:

### ModalLogic

#### Methods:

- `necessitation() -> Rule`

- `distribution_axiom() -> Rule`

- `possibility_axiom() -> Rule`

- `modal_modus_ponens() -> Rule`

- `t_schema() -> Rule`

---

# Module: symlogos.axiom_set

## Classes:

### AxiomSet

#### Methods:

- `__init__(self: unknown) -> None`

- `add_axiom(self: unknown, axiom: Proposition) -> None`

- `remove_axiom(self: unknown, axiom: Proposition) -> None`

- `__iter__(self: unknown) -> unknown`

- `__len__(self: unknown) -> int`

- `__contains__(self: unknown, axiom: Proposition) -> bool`

- `__repr__(self: unknown) -> str`

---

# Module: symlogos.quantified_logic

## Classes:

### QuantifiedLogic

#### Methods:

- `existential_instantiation() -> Rule`

- `barcan_formula() -> Rule`

---

# Module: symlogos.rules

## Classes:

### Rule

#### Methods:

- `__init__(self: unknown, name: str, premises: List[Basic], conclusion: Basic) -> None`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> str`

- `apply(self: unknown) -> LogicalExpression`

- `to_nnf(self: unknown) -> 'Rule'`

## Functions:

- `check_consistency() -> unknown`

- `check_validity() -> unknown`

---

# Module: symlogos.tableau_prover

## Classes:

### TableauNode

#### Methods:

- `__init__(self: unknown, signed_formula: SignedFormula, parent: Optional[TableauNode]) -> None`

- `add_child(self: unknown, signed_formula: unknown) -> unknown`

- `get_next_fresh_constant_index(self: unknown) -> unknown`

- `get_next_fresh_variable_index(self: unknown) -> int`

### TableauProver

#### Methods:

- `__init__(self: unknown) -> unknown`

- `is_sound(self: unknown, premises: unknown, conclusion: unknown) -> unknown`

- `tableau_expansion(self: unknown, signed_formula: unknown, depth: unknown, max_depth: unknown) -> unknown`

- `_is_tableau_closed(self: unknown, node: unknown) -> unknown`

### TableauRule

#### Methods:

- `__init__(self: unknown, signed_formula: SignedFormula) -> None`

- `is_applicable(self: unknown) -> unknown`

- `apply(self: unknown) -> unknown`

### AlphaRule

#### Methods:

- `__init__(self: unknown, signed_formula: SignedFormula) -> None`

- `__hash__(self: unknown) -> unknown`

- `is_applicable(self: unknown) -> bool`

- `apply(self: unknown) -> List[SignedFormula]`

### BetaRule

#### Methods:

- `__init__(self: unknown, signed_formula: SignedFormula) -> None`

- `__hash__(self: unknown) -> unknown`

- `is_applicable(self: unknown) -> bool`

- `apply(self: unknown) -> List[SignedFormula]`

### GammaRule

#### Methods:

- `__init__(self: unknown, signed_formula: SignedFormula) -> None`

- `__hash__(self: unknown) -> unknown`

- `is_applicable(self: unknown) -> bool`

- `apply(self: unknown, node: TableauNode) -> List[TableauNode]`

### DeltaRule

#### Methods:

- `__init__(self: unknown, signed_formula: SignedFormula) -> None`

- `__hash__(self: unknown) -> unknown`

- `is_applicable(self: unknown) -> unknown`

- `apply(self: unknown, node: TableauNode) -> List[TableauNode]`

---

# Module: symlogos.connectives

## Classes:

### Implication

#### Methods:

- `__init__(self: unknown, antecedent: Union['Proposition', 'Necessity', Term], consequent: Union['Proposition', 'Necessity', Term]) -> None`

- `__hash__(self: unknown) -> unknown`

- `__eq__(self: unknown, other: 'Implication') -> bool`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> unknown`

- `substitute(self: unknown, variable: unknown, replacement: unknown) -> unknown`

- `evaluate(self: unknown, valuation: unknown) -> unknown`

- `simplify(self: unknown) -> unknown`

- `match(self: unknown, other: 'Implication') -> Dict[Any, Any]`

- `to_nnf(self: unknown) -> 'Or'`

### And

#### Methods:

- `__init__(self: unknown, left: Any, right: Union[And, Term, Or, 'Proposition', Not]) -> None`

- `__hash__(self: unknown) -> unknown`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> unknown`

- `substitute(self: unknown, variable: 'Proposition', replacement: 'Proposition') -> 'And'`

- `substitute_all_terms(self: unknown, term_replacement_dict: Dict[Any, Any]) -> 'And'`

- `evaluate(self: unknown, valuation: unknown) -> unknown`

- `__eq__(self: unknown, other: 'And') -> bool`

- `simplify(self: unknown) -> Union['Proposition', bool, And]`

- `match(self: unknown, other: 'And', bindings: None) -> Dict[Any, Any]`

- `to_nnf(self: unknown) -> 'And'`

### Or

#### Methods:

- `__init__(self: unknown, left: Union['Proposition', And, Or, Not], right: Union['Proposition', Or, Not, And]) -> None`

- `__hash__(self: unknown) -> unknown`

- `__repr__(self: unknown) -> unknown`

- `__eq__(self: unknown, other: 'Or') -> bool`

- `variables(self: unknown) -> unknown`

- `substitute_all_terms(self: unknown, term_replacement_dict: Dict[Any, Any]) -> 'Or'`

- `match(self: unknown, other: 'Or', bindings: None) -> Dict[Any, Any]`

- `to_nnf(self: unknown) -> 'Or'`

### Not

#### Methods:

- `__init__(self: unknown, expr: Union[And, bool, Or, 'Proposition', Not]) -> None`

- `__eq__(self: unknown, other: 'Not') -> bool`

- `__hash__(self: unknown) -> unknown`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> unknown`

- `substitute(self: unknown, variable: 'Proposition', replacement: 'Proposition') -> 'Not'`

- `substitute_all_terms(self: unknown, term_replacement_dict: Dict[Any, Any]) -> 'Not'`

- `evaluate(self: unknown, valuation: unknown) -> unknown`

- `simplify(self: unknown) -> Union['Proposition', bool, Not]`

- `__eq__(self: unknown, other: 'Not') -> bool`

- `match(self: unknown, other: 'Not') -> Dict[Any, Any]`

- `to_nnf(self: unknown) -> 'Not'`

---

# Module: symlogos.classical_propositional_logic

## Classes:

### ClassicalPropositionalLogic

#### Methods:

- `modus_ponens() -> Rule`

- `modus_tollens() -> Rule`

- `disjunction_introduction() -> Rule`

- `disjunction_elimination() -> Rule`

- `conjunction_introduction() -> Rule`

- `conjunction_elimination1() -> Rule`

- `conjunction_elimination2() -> Rule`

- `commutativity_and() -> Rule`

- `commutativity_or() -> Rule`

- `associativity_and() -> Rule`

- `associativity_or() -> Rule`

- `idempotency_and() -> Rule`

- `idempotency_or() -> Rule`

- `double_negation_elimination() -> Rule`

- `distribution_and_over_or() -> Rule`

- `distribution_or_over_and() -> Rule`

- `absorption_and() -> Rule`

- `absorption_or() -> Rule`

- `negation_and_to_or() -> Rule`

- `negation_or_to_and() -> Rule`

- `implication_to_or() -> Rule`

---

# Module: symlogos.functions_and_predicates

## Classes:

### Predicate

#### Methods:

- `__new__(cls: Type[Predicate], name: Union[sympy.core.symbol.Symbol, str]) -> 'Predicate'`

- `__eq__(self: unknown, other: 'Predicate') -> bool`

- `__hash__(self: unknown) -> unknown`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> unknown`

- `substitute(self: unknown, mapping: Dict[Term, Term]) -> 'Predicate'`

- `substitute_all_terms(self: unknown, term_replacement_dict: Dict[Term, Term]) -> 'Predicate'`

- `evaluate(self: unknown, valuation: unknown) -> unknown`

- `match(self: unknown, other: 'Predicate') -> Dict[Term, Term]`

- `is_atomic(self: unknown) -> unknown`

- `to_nnf(self: unknown) -> 'Predicate'`

### HigherOrderFunction

#### Methods:

- `__new__(cls: Type[HigherOrderFunction], name: str, arg_function: Optional[HigherOrderFunction], return_function: Optional[Union[Predicate, HigherOrderFunction]]) -> 'HigherOrderFunction'`

- `name(self: unknown) -> sympy.core.symbol.Symbol`

- `arg_function(self: unknown) -> unknown`

- `arg_function(self: unknown, value: unknown) -> unknown`

- `return_function(self: unknown) -> unknown`

- `return_function(self: unknown, value: unknown) -> unknown`

- `__str__(self: unknown) -> str`

- `__repr__(self: unknown) -> str`

- `match(self: unknown, expr: unknown) -> unknown`

### FunctionApplication

#### Methods:

- `__init__(self: unknown, function_symbol: Union[HigherOrderFunction, str]) -> None`

- `__str__(self: unknown) -> str`

- `__eq__(self: unknown, other: 'FunctionApplication') -> bool`

- `substitute(self: unknown, mapping: unknown) -> unknown`

- `variables(self: unknown) -> unknown`

- `match(self: unknown, other: unknown) -> unknown`

---

