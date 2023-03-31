# Tableaux and Negation Normal Form (NNF)

In this document, we discuss the tableaux method in the context of propositional and first-order logic, and why using Negation Normal Form (NNF) is beneficial for the tableaux method.

## Tableaux Method

The tableaux method is a proof procedure for checking the satisfiability of logical formulas. It systematically constructs a tree-like structure called a tableau, which represents possible models of the given formula. Each node in the tree corresponds to a subformula of the original formula. The tableaux method aims to either find a branch in the tableau that corresponds to a satisfying model or demonstrate that no such model exists, proving that the formula is unsatisfiable.

## Negation Normal Form (NNF)

Negation Normal Form is a way of transforming logical formulas such that negations only appear directly applied to atomic propositions, and the only logical connectives used are conjunction (∧) and disjunction (∨). Formulas in NNF are structurally simpler than their equivalent formulas in other normal forms, which can be advantageous for certain proof methods, including the tableaux method.

## Benefits of NNF for Tableaux

NNF simplifies the structure of formulas, making the search for proofs or counterexamples more efficient within the tableaux method. The simplified structure of NNF formulas allows the tableaux method to systematically explore possible models and contradictions more efficiently, ultimately leading to a more effective proof search.

When a formula is in NNF, the tableaux method can easily identify and handle the different types of subformulas it encounters during the proof search:

1. **Disjunctions (∨)**: When a disjunction is encountered, the method can split the branch into two separate branches, each representing one of the disjuncts.
2. **Conjunctions (∧)**: When a conjunction is encountered, the method can simply add both conjuncts to the current branch.

By using NNF, the tableaux method can more effectively navigate the tableau tree and search for proofs or counterexamples, making it a better choice for handling formulas within this proof method.
