# Tableau Proving Method

The tableau proving method is a technique used in automated theorem proving to check the satisfiability of a given formula. It's based on the idea of breaking complex formulas into smaller, more manageable subformulas. The method systematically explores the space of possible interpretations of the given formula by applying specific rules, known as tableau expansion rules, to derive new formulas. The process continues until a contradiction (an unsatisfiable set of formulas) is found, or until all possibilities have been exhausted.

## Rule Types

There are several types of tableau expansion rules, including:

### 1. Alpha (α) Rules

Alpha rules are used to break down conjunctions and signed formulas into simpler components. They correspond to cases where the truth value of a formula can be determined directly from the truth values of its subformulas. For example:

- T(φ ∧ ψ) → T(φ), T(ψ)
- F(φ ∨ ψ) → F(φ), F(ψ)
- F(φ → ψ) → T(φ), F(ψ)
- T(¬φ) → F(φ)
- F(¬φ) → T(φ)

### 2. Beta (β) Rules

Beta rules are used to handle disjunctions and implications. They correspond to cases where the truth value of a formula depends on the truth values of its subformulas. For example:

- T(φ ∨ ψ) → T(φ) or T(ψ)
- F(φ ∧ ψ) → F(φ) or F(ψ)
- T(φ → ψ) → F(φ) or T(ψ)

### 3. Gamma (γ) Rules

Gamma rules are used to handle universal quantifiers. They allow for the introduction of new terms (constants or variables) that satisfy the quantified formula. For example:

- T(∀x. φ(x)) → T(φ(c)) for a fresh constant c
- F(∃x. φ(x)) → F(φ(c)) for a fresh constant c

### 4. Delta (δ) Rules

Delta rules are used to handle existential quantifiers. They allow for the introduction of new terms (constants or variables) that satisfy the quantified formula. For example:

- T(∃x. φ(x)) → T(φ(c)) for a fresh constant c
- F(∀x. φ(x)) → F(φ(c)) for a fresh constant c

## Tableau Proving Process

The tableau proving process involves the following steps:

1. Convert the input formula into an equivalent formula in negation normal form (NNF).
2. Create a signed formula by associating the input formula with a truth value (True or False).
3. Initialize the tableau with the signed formula.
4. Apply tableau expansion rules to the signed formulas in the tableau until a contradiction is found or until all possibilities have been exhausted.
5. If a contradiction is found, the input formula is unsatisfiable. Otherwise, the input formula is satisfiable.

The tableau proving method can be extended to handle higher-order logics and modal logics by adding specific rules for these logics. The general approach remains the same, but the set of tableau expansion rules is expanded to include rules specific to the logic being considered.
